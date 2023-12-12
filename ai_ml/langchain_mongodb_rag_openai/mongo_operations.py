from openai import OpenAI
from pymongo import MongoClient
from pymongo.server_api import ServerApi


def getMongoClient():
    f =  open('api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            print(uri)
            client = MongoClient(uri, server_api=ServerApi('1'))

    return client

#print(getMongoClient())