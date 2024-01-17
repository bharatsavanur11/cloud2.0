from langchain.chains import RetrievalQA
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from openai import OpenAI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from md_exp_configs.openai_config import get_openai_key
from md_exp_configs.mongo_configs import get_mongo_uri, get_mongo_client


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


def search_using_langchain(query):
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
    dbName = "langchain_demo"
    collectionName = "text_data_2"
    collection = client[dbName][collectionName]
    index_name = "lang_demo_test"

    api_key = get_openai_key()

    # Define the text embedding model
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # Initialize the Vector Store
    vectorStore = MongoDBAtlasVectorSearch(collection, embeddings, index_name=index_name)

    #as_output = vectorStore.similarity_search(query, )

    llm = OpenAI(api_key=api_key)

    retriever = vectorStore.as_retriever()

    # Load "stuff" documents chain. Stuff documents chain takes a list of documents,
    # inserts them all into a prompt and passes that prompt to an LLM.

    qa = RetrievalQA.from_chain_type(llm, chain_type="refine", retriever=retriever)

    # Execute the chain
    retriever_output = qa.run(query)

    # Return Atlas Vector Search output, and output generated using RAG Architecture
    return retriever_output
