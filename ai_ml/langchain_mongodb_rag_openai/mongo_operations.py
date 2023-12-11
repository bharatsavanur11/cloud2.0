from gettext import install

import streamlit as st
import pandas as pd

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

uri = "mongodb+srv://hellobharat:hellobharat1@sandbox.daamc.mongodb.net/?retryWrites=true&w=majority"


def getMongoClient():
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text})

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()


def search(query):
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client.sample_mflix
    collection = db.movies

    # result = collection.find().limit(10)
    # df = pd.DataFrame(result)
    # df = pd.DataFrame(list(collection.find())
    # st.dataframe(df, use_container_width=False)
    # for doc in collection.find():
    # st.write(doc)
        # query = "imaginary characters from outer space at war"

    results = collection.aggregate([
        {"$vectorSearch": {
            "queryVector": generate_embedding(query),
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": 4,
            "index": "plot_vector_index",
        }}
    ])

    return results

print(getMongoClient())