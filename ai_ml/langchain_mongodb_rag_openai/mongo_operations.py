

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests


def getMongoClient():
    f =  open('api_key')
    lines = f.readlines()
    for line in lines:
        #print(line)
        tokens = line.split("=")
        print(tokens[1].strip())
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            return uri

print(getMongoClient())