import json

from configs.redis_config import get_redis_config, get_redis_client

redis_host, redis_port, redis_password = get_redis_config()
print(redis_host, redis_port, redis_password)
client = get_redis_client(redis_host, redis_port, redis_password)
for key in client.scan_iter():
    val = client.hget(key,'content').decode('utf-8')
    print(val)