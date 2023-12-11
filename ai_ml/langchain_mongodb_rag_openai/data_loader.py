from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain.llms import OpenAI

from mongo_operations import getMongoClient
from openai_config import  getOpenAiClient, getOpenAIKey

client = getMongoClient()

dbName = "langchain_demo"
collectionName = "text_data"
collection = client[dbName][collectionName]

print("Loading Data")
# Initialize the DirectoryLoader
loader = DirectoryLoader('/Users/bharatsavanur/Desktop/projects/personal_git/cloud-2.0/ai_ml/ lang-chain/lang_chain/langchain_mongodb_rag_openai/data')
documents = loader.load()
#for document in documents:

 #   print(document)
#print(data)
# Define the OpenAI Embedding Model we want to use for the source data
# The embedding model is different from the language generation model

print("Starting embeeding process")
embeddings = OpenAIEmbeddings(openai_api_key=getOpenAIKey())

print(embeddings)
print("Vectorizing data")
# Initialize the VectorStore, and
# vectorise the text from the documents using the specified embedding model, and insert them into the specified MongoDB collection

vectorStore = MongoDBAtlasVectorSearch.from_documents( documents, embeddings, collection=collection )
