from openai import OpenAI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

file_path = os.path.join(os.path.dirname(__file__), '../..', 'md_exp_configs', 'api_key')


def get_mongo_client():
    f = open(file_path)
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            print(uri)
            client = MongoClient(uri, server_api=ServerApi('1'))

    return client


def get_mongo_uri():
    f = open(file_path)
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            print(uri)
            # client = MongoClient(uri, server_api=ServerApi('1'))

    return uri

# Tested it works.
#print(get_mongo_uri())
