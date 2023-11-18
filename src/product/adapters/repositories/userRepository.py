from abc import ABC

from account.domain.entities.UserEntity import UserEntity
from backbone.adapter.abstract_repository import AbstractRepository
from backbone.adapter.abstract_sqlalchemy_repository import AbstractSqlalchemyRepository



class UserRepository(AbstractSqlalchemyRepository):
    @property
    def model(self):
        return UserEntity
