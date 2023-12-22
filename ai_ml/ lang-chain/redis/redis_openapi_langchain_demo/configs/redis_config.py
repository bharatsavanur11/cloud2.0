import redis
from langchain.vectorstores.redis import Redis as RedisVDB

from configs.openai_config import get_embeddings


def get_redis_config():
    redis_host = ''
    redis_port = ''
    redis_password = ''
    f = open(
        '/Users/bharatsavanur/Desktop/projects/personal_git_2/ai_ml/ lang-chain/redis/redis_openapi_langchain_demo/configs/api_key')
    lines = f.readlines()
    for line in lines:
        tokens = line.split("==")
        if tokens[0].strip() == 'redis.host':
            redis_host = tokens[1].strip()
        if tokens[0].strip() == 'redis.password':
            redis_password = tokens[1].strip()
        if tokens[0].strip() == 'redis.port':
            redis_port = tokens[1].strip()
    return redis_host, redis_port, redis_password


def get_redis_client(redis_host, redis_port, redis_password):
    return redis.Redis(
        host=redis_host,
        port=redis_port,
        password=redis_password
    )


def get_redis_vector_store():
    redis_host, redis_port, redis_password = get_redis_config()
    REDIS_URL = f"redis://:{redis_password}@{redis_host}:{redis_port}"
    vectorstore = RedisVDB.from_existing_index(
        embedding=get_embeddings(),
        index_name='open_ai_embeddings',
        redis_url=REDIS_URL
    )
    return vectorstore
