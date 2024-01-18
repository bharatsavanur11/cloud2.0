from langchain.chains import RetrievalQA
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from md_exp_configs.mongo_configs import get_mongo_uri, get_mongo_client
from md_exp_configs.openai_config import get_openai_key


def generate_embedding(text_to_embed):
    # Embed a line of text
    client = OpenAI(api_key=get_openai_key())
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=[text_to_embed]
    )
    # Extract the AI output embedding as a list of floats
    embedding = response.data[0].embedding
    print(embedding)
    return embedding


def mongo_db_search(query):
    client = MongoClient(get_mongo_uri(), server_api=ServerApi('1'))
    db = client.langchain_demo
    collection = db.text_data_1
    results = collection.aggregate([
        {"$vectorSearch": {
            "queryVector": generate_embedding(query),
            "path": "embedding",
            "numCandidates": 100,
            "limit": 4,
            "index": "lang_demo_test",
        }}
    ])


def query_data(query):
    client = get_mongo_client()
    db_name = "langchain_demo"
    collection_name = "text_data_2"
    collection = client[db_name][collection_name]
    index_name = "default"

    api_key = get_openai_key()

    # Define the text embedding model
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # Initialize the Vector Store
    vector_store = MongoDBAtlasVectorSearch(collection, embeddings, index_name=index_name)
    print(query)
    as_output = vector_store.similarity_search(query, K=1)
    print("Output ", as_output)

    llm = OpenAI(openai_api_key=api_key, temperature=0)

    retriever = vector_store.as_retriever()

    # Load "stuff" documents chain. Stuff documents chain takes a list of documents,
    # inserts them all into a prompt and passes that prompt to an LLM.

    qa = RetrievalQA.from_chain_type(llm, chain_type="refine", retriever=retriever)

    # Execute the chain
    retriever_output = qa.run(query)

    # Return Atlas Vector Search output, and output generated using RAG Architecture
    return as_output,retriever_output
