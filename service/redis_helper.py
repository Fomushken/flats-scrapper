import redis.asyncio as redis

from config import load_config

redis_client = None

async def get_redis():
    config = load_config()
    global redis_client
    if not redis_client:
        redis_client = redis.from_url(config.redis.url)
    return redis_client

async def add_subscriber(user_id):
    redis_client = await get_redis()
    await redis_client.sadd('subscribers', user_id)

async def get_subscribers():
    redis_client = await get_redis()
    return await redis_client.smembers('subscribers')

async def remove_subscriber(user_id):
    redis_client = await get_redis()
    await redis_client.srem('subscribers', user_id)