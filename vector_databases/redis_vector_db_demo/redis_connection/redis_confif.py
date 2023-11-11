import redis
import numpy as np
import pandas as pd
import requests
from redis.commands.search.field import (
    NumericField,
    TagField,
    TextField,
    VectorField
)

client = redis.Redis(
    host='redis-16718.c91.us-east-1-3.ec2.cloud.redislabs.com',
    port=16718,
    password=''
)

client.set('foo', 'bar')

from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import SentenceTransformer

url = "https://raw.githubusercontent.com/bsbodden/redis_vss_getting_started/main/data/bikes.json"
response = requests.get(url)
bikes = response.json()
# print(bikes)

##
pipeline = client.pipeline()

for i, bike in enumerate(bikes, start=1):
    redis_key = f"bikes:{i:03}"
    pipeline.json().set(redis_key, "$", bike)
    # print(redis_key)
res = pipeline.execute()

## Starting the machine learning tasks

embedder = SentenceTransformer('msmarco-distilbert-base-v4')

keys = sorted(client.keys("bikes:*"))
print(keys)

descriptions = client.json().mget(keys, "$.description")
descriptions = [item for sublist in descriptions for item in sublist]
embeddings = embedder.encode(descriptions).astype(np.float32).tolist()
VECTOR_DIMENSION = len(embeddings[0])
#print(embeddings)
#print(VECTOR_DIMENSION)

pipeline = client.pipeline()
for key, embedding in zip(keys, embeddings):
    pipeline.json().set(key, '$.description_embeddings', embedding)
pipeline.execute()

intermediate_result = client.json().get("bikes:010")

schema = (
    TextField("$.model", no_stem=True, as_name="model"),
    TextField("$.brand", no_stem=True, as_name="brand"),
    NumericField("$.price", as_name="price"),
    TagField("$.type", as_name="type"),
    TextField("$.description", as_name="description"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": VECTOR_DIMENSION,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

# Need to uncomment it when running it for the first time
# When index was created.
#definition = IndexDefinition(prefix=["bikes:"], index_type=IndexType.JSON)
#index_res = client.ft("idx:bikes_vss").create_index(
 #   fields=schema, definition=definition
#)

#print(index_res)

info = client.ft("idx:bikes_vss").info()
num_docs_indexed = info["num_docs"]
print(f"{num_docs_indexed}")

#############

queries = [
    "Bike for small kids",
    "Best Mountain bikes for kids",
    "Cheap Mountain bike for kids",
    "Female specific mountain bike",
    "Road bike for beginners",
    "Commuter bike for people over 60",
    "Comfortable commuter bike",
    "Good bike for college students",
    "Mountain bike for beginners",
    "Vintage bike",
    "Comfortable city bike",
]

encoded_queries = embedder.encode(queries)
len(encoded_queries)
print(len(encoded_queries))


query = (
    Query('(*)=>[KNN 3 @vector $query_vector as vector_score]')
    .sort_by('vector_score')
    .return_fields('vector_score', 'id', 'brand', 'model', 'description')
    .dialect(2)
)


def create_query_table(query, queries, encoded_queries, extra_params=None):
    if extra_params is None:
        extra_params = {}
    results_list = []
    for i, encoded_query in enumerate(encoded_queries):
        result_docs = (
            client.ft("idx:bikes_vss")
            .search(
                query,
                {
                    "query_vector": np.array(
                        encoded_query, dtype=np.float32
                    ).tobytes()
                }
                | extra_params,
                )
            .docs
        )
       # print(result_docs)
        for doc in result_docs:
            vector_score = round(1 - float(doc.vector_score), 2)
            results_list.append(
                {
                    "query": queries[i],
                    "score": vector_score,
                    "id": doc.id,
                    "brand": doc.brand,
                    "model": doc.model,
                    "description": doc.description,
                }
            )
    print(results_list)

create_query_table(query, queries, encoded_queries)
