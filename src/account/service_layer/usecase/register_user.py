from account.adapters.data_models import UserEntity
from account.domain import commands
from account.service_layer.resources.user import UserResource
from backbone.infrastructure.databases.redis.connection import RedisConnection
from backbone.service_layer.general_types import Command
from backbone.services.auth import create_access_token, get_current_user, decode, generate_access_token
from unit_of_work import UnitOfWork


async def register_user(*, command: commands.RegisterCommand, uow=UnitOfWork):
    """Register a user.

    Creates a new user entity using the provided command and adds it to the unit of work session.
    Commits the changes to the database and refreshes the user entity.
    Generates an access token for the user.

    Args:
        command: The register command containing the user data.
        uow: The unit of work.

    Returns:
        The user resource representing the registered user.

    """
    async with uow() as uow:
        user = UserEntity.create(**command.model_dump())
        uow.session.add(user)
        await uow.session.commit()
        print('aaaa')
        await uow.session.refresh(user)

    await generate_access_token(user.id)


    return UserResource().optional(user)
