# from __future__ import annotations
#
# from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
#
import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from account.adapters import repositories as account_repo
from account.adapters.data_models import UserEntity
from backbone.infrastructure.databases.postgres_connection import get_db


# from backbone.infrastructure.databases.postgres_connection import DEFAULT_ENGIN, DEFAULT_SESSION_FACTORY
# from backbone.service_layer.abstract_unit_of_work import AbstractUnitOfWork
#
# async def create_unit_of_work(session_factory=DEFAULT_SESSION_FACTORY):
#     session = async_sessionmaker(session_factory, class_=AsyncSession)()
#     await session.__aenter__()
#     user = account_repo.UserRepository(session)
#     return session, user
#
# class UnitOfWork(AbstractUnitOfWork):
#     def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
#         self.session_factory = session_factory


# async def __aenter__(self):
#     self.session, self.user = await create_unit_of_work()
# self.session = async_sessionmaker(
#     bind=DEFAULT_ENGIN
#      , expire_on_commit=False
#      , class_=AsyncSession
#  )
# #self.session = DEFAULT_SESSION_FACTORY
# await self.session.__aenter__()
# self.user = account_repo.UserRepository(self.session)

# return super().__aenter__()
# pass

# async def __aexit__(self, *args):
#     super().__aexit__(*args)
#     self.session.close()


class UnitOfWork(object):
    def __init__(self, postgres_session_factory: AsyncSession = Depends(get_db)):
        self.session_factory = postgres_session_factory

    async def __aenter__(self):
        session = await get_db()

        async with session as conn:
            self.session = conn
            self.user = account_repo.UserRepository(self.session)
            return self

    async def __aexit__(self, *args):
        await self.session.close()

    async def get(self, id):
        result = sa.select(UserEntity).where(UserEntity.is_active == True)
        a = await self.session.scalar(result)

    async def rollback(self):
        self.session.expunge_all()


