from openai import OpenAI
from pymongo import MongoClient
from pymongo.server_api import ServerApi


def get_mongo_client():
    f =  open('api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            print(uri)
            client = MongoClient(uri, server_api=ServerApi('1'))

    return client

def get_mongo_uri():
    f =  open('api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            print(uri)
            #client = MongoClient(uri, server_api=ServerApi('1'))

    return uri

#print(getMongoClient())