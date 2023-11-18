from account.service_layer.resources.user import UserResource
from backbone.infrastructure.databases.redis.connection import RedisConnection
from backbone.service_layer.general_types import Command
from backbone.services.auth import create_access_token, get_current_user, decode
from unit_of_work import UnitOfWork


async def register_user(*, command: Command, uow=UnitOfWork):
    # raise LogicalValidationException("aaaaa", "bbbb", "cccc")

    async with uow() as uow:
        user = await uow.user.create(**command.model_dump())

    async with RedisConnection() as r:
        generate_token = create_access_token(user.id)
        insert_to_redis = await r.set_value(generate_token, generate_token)

        a = await r.get_value(generate_token)
        print(a)


    return UserResource().optional(user)

        # return user.normalize_dict()
