from account.adapters.data_models.userentity import UserEntity
from backbone.adapter.abstract_sqlalchemy_repository import AbstractSqlalchemyRepository


class UserRepository(AbstractSqlalchemyRepository):
    @property
    def model(self):
        return UserEntity

    async def find_by_mobile(self, mobile):
        result = self.query.where(UserEntity.mobile == mobile)
        data = await self.session.scalar(result)
        print(data)
        return data
