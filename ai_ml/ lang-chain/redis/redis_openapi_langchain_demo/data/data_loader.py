from typing import List

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from configs.redis_config import get_redis_config, get_redis_client
from langchain.vectorstores.redis import Redis as RedisVDB
from configs.openai_config import get_embeddings,get_openai_client
from langchain.schema import Document


print("Loading Data")


def load_docs():
    # Initialize the DirectoryLoader
    loader = DirectoryLoader(
        '/Users/bharatsavanur/Desktop/projects/personal_git_2/ai_ml/ lang-chain/redis/redis_openapi_langchain_demo/data',
        glob="**/*.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=4096, chunk_overlap=200)
    documents1 = text_splitter.split_documents(documents)
    print(len(documents1))
    return documents1


def get_vectorstore(documents: List[Document] = None) -> "RedisVBD":
    """Create the Redis vectorstore."""
    print(documents)
    redis_host, redis_port, redis_password = get_redis_config()
    embeddings = get_embeddings()
    REDIS_URL = f"redis://:{redis_password}@{redis_host}:{redis_port}"
    try:
        vectorstore = RedisVDB.from_existing_index(
            embedding=embeddings,
            index_name='open_ai_embeddings',
            redis_url=REDIS_URL        )
        return vectorstore
    except:
        pass

    vectorstore = RedisVDB.from_documents(
        documents=documents,
        embedding=embeddings,
        index_name='open_ai_embeddings',
        redis_url=REDIS_URL
    )
    return vectorstore


documents = load_docs()


redis_host, redis_port, redis_password = get_redis_config()
#print(redis_host, redis_port, redis_password)
client = get_redis_client(redis_host, redis_port, redis_password)
get_openai_client()
#get_vectorstore(documents)
print(client.ping())





