from account.adapters.data_models.user import User
from backbone.adapter.abstract_sqlalchemy_repository import AbstractSqlalchemyRepository


class UserRepository(AbstractSqlalchemyRepository):
    @property
    def model(self):
        # pass
        return User

    # first_name = None, last_name = None, username = None, mobile = None, email = None, type = None,
    # is_active = None
    async def create(self, first_name=None, last_name=None, username=None, mobile=None, email=None, type=None,
                     is_active=None):
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.mobile = mobile
        user.email = email
        user.type = type
        user.is_active = is_active

        # print(first_name)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
