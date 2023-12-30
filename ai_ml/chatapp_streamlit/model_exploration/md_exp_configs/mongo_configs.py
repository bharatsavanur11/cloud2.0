from openai import OpenAI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

file_path =  os.path.join(os.path.dirname(__file__), '..', 'md_exp_configs', 'api_key')
'''
    The below index needs to be created for RAG implementation of the OpenAI Api.
    In MongoDB Cloud Atlas.
    
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "embedding": {
        "dimensions": 1536,
        "similarity": "cosine",
        "type": "knnVector"
      }
    }
  }
}

As a part of this project, the knn index on the sample_analytics.transactions database has been indexed.

'''
def get_mongo_client():
    f =  open(file_path)
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            print(uri)
            client = MongoClient(uri, server_api=ServerApi('1'))
            return client

    return None


def get_mongo_uri():
    f =  open(file_path)
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'mongo_url':
            uri = tokens[1].strip()
            print(uri)
            #client = MongoClient(uri, server_api=ServerApi('1')
            return uri
    return None

if __name__ == '__main__':
    print(get_mongo_uri())

#print(getMongoClient())