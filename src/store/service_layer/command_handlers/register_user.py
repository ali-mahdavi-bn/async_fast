from account.domain import commands
from unit_of_work import UnitOfWork


def register_user(command: commands.RegisterUser, uow: UnitOfWork):
    with uow:
        a = uow.user.find_by_id(1)
        b = uow.user.find_by_id(1)

        return a
