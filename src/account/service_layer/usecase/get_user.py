from redis.asyncio import Redis

from backbone.configs import config
from backbone.infrastructure.databases.redis.connection import RedisConnection
from backbone.service_layer.general_types import Command
from unit_of_work import UnitOfWork


async def get_user(*, uow=UnitOfWork):
    # async with uow() as uow:
    #     user = await uow.user.find_by_id(3)
    #     return user
    pass