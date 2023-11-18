from account.domain.entities import UserEntity
from account.service_layer.resources.user import UserResource
from unit_of_work import UnitOfWork


def register_user(uow: UnitOfWork):
    with uow:
        a: UserEntity = uow.user.find_by_id(1)
        return UserResource(uow).make(model=a)
        # a.normalize_dict()
        # print(a.id)
        # print(a.uuid)
        # print(a.first_name)
    # return UserResource(uow).make(model=a)
    #     return a
