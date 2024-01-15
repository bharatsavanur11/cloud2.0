from openai import OpenAI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from md_exp_configs.openai_config import get_openai_key
from md_exp_configs.mongo_configs import get_mongo_uri


def generate_embedding(text_to_embed):
    # Embed a line of text
    client = OpenAI(api_key=get_openai_key())
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=[text_to_embed]
    )
    print(response)
    # Extract the AI output embedding as a list of floats
    embedding = response.data[0].embedding
    print(embedding)
    return embedding


def search(query):
    client = MongoClient(get_mongo_uri(), server_api=ServerApi('1'))
    db = client.langchain_demo
    collection = db.text_data_1

    # result = collection.find().limit(10)
    # df = pd.DataFrame(result)
    # df = pd.DataFrame(list(collection.find())
    # st.dataframe(df, use_container_width=False)
    # for doc in collection.find():
    # st.write(doc)
    # query  = "imaginary characters from outer space at war"

    results = collection.aggregate([
        {"$vectorSearch": {
            "queryVector": generate_embedding(query),
            "path": "embedding",
            "numCandidates": 100,
            "limit": 4,
            "index": "lang_demo_test",
        }}
    ])

    return results


# results = search("What is primary focus of the budget this year?")
# for data in results:
#     print(data)
