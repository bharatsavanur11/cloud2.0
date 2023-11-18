from gettext import install

import streamlit as st
import pandas as pd

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

uri = "mongodb+srv://hellobharat:hellobharat@sandbox.daamc.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.sample_mflix
collection = db.movies

#st.write("My first Stream Lit app")
for doc in collection.find():
    st.write(doc)

