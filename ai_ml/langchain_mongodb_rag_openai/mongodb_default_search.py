from gettext import install

import streamlit as st
import pandas as pd

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

from openai import OpenAI

uri = "mongodb+srv://hellobharat:hellobharat@sandbox.daamc.mongodb.net/?retryWrites=true&w=majority"


def generate_embedding(text_to_embed):
    # Embed a line of text
    client = OpenAI()
    response = client.embeddings.create(
        model= "text-embedding-ada-002",
        input=[text_to_embed]
    )
    # Extract the AI output embedding as a list of floats
    embedding = response["data"][0]["embedding"]

    return embedding


def search(query):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.langchain_demo
    collection = db.text_data2

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
            "index": "plot_vector_index",
        }}
    ])

    return results

