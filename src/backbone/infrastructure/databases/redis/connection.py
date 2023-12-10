from typing import Optional

from redis.asyncio import Redis

from backbone.configs import config


# class RedisConnection:
#     _connection = None
#     redis_host: str = config.REDIS_HOST
#     redis_port: int = config.REDIS_PORT
#     redis_db: int = 0
#
#     @classmethod
#     async def get_connection(cls):
#         if not cls._connection:
#             cls._connection = await Redis(host=cls.redis_host, port=cls.redis_port, db=cls.redis_db,
#                                           decode_responses=True, retry_on_timeout=True)
#         return cls._connection
#
#     @classmethod
#     async def get_value(cls, key):
#         await cls.get_connection()
#         return await cls._connection.get(key)
#
#     @classmethod
#     def exists_key(cls, key):
#         cls.get_connection()
#         return True if cls._connection.exists(key) == 1 else False
#
#     @classmethod
#     async def set_value(cls, key, value, exp: Optional[int] = None):
#         await cls.get_connection()
#         cls._connection.set(key, value)
#         if exp:
#             cls._connection.expire(key, time=exp)
#
#     @classmethod
#     def delete_key(cls, key):
#         cls.get_connection()
#         cls._connection.delete(key)
#
#     @classmethod
#     def get_keys_with_prefix(cls, prefix: str):
#         cls.get_connection()
#         return [item.decode("utf-8") for item in cls._connection.keys(prefix + "*")]
#
#     @classmethod
#     def push_values(cls, key, values: list, exp: Optional[int] = None):
#         cls.get_connection()
#         cls._connection.lpush(key, *values)
#         if exp:
#             cls._connection.expire(key, time=exp)
#
#     @classmethod
#     def get_all_list_values(cls, key: str):
#         cls.get_connection()
#         values_list = cls._connection.lrange(key, 0, -1)
#         values_list = [item.decode("utf-8") for item in values_list]
#         return values_list


class RedisConnection:
    _connection = None
    redis_host: str = config.REDIS_HOST
    redis_port: int = config.REDIS_PORT
    redis_db: int = 0

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        conn = await self.get_connection()
        await conn.close()

    async def get_connection(cls):
        if not cls._connection:
            cls._connection = await Redis(host=cls.redis_host, port=cls.redis_port, db=cls.redis_db,
                                          decode_responses=True, retry_on_timeout=True)
        return cls._connection

    async def set_value(cls, key, value, exp: Optional[int] = None):
        await cls.get_connection()
        await cls._connection.set(key, value)
        if exp:
            await cls._connection.expire(key, time=exp)

    async def get_value(cls, key):
        await cls.get_connection()
        return await cls._connection.get(key)

    async def exists(cls, key):
        await cls.get_connection()
        return True if await cls._connection.exists(key) == 1 else False

    async def ttl(cls, key):
        await cls.get_connection()
        return await cls._connection.ttl(key)

    async def set_and_get(cls, key, value):
        await cls.set_value(key=key, value=value)
        await cls.get_value(key=key)

    async def close(cls):
        await cls._connection.close()
