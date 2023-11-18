import datetime
from uuid import UUID

from backbone.adapter.abstract_entity import BaseEntity


class UserDetailEntity(BaseEntity):
    id: int
    uuid: UUID
    user_id: int
    nationalCode: int
    gender: int
    birth: datetime.datetime
    lastLogin: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, id=None, uuid=None, updated_at=None, user_id=None, nationalCode=None, gender=None,
                 birth=None, lastLogin=None, created_at=None):
        self.id = id
        self.uuid = uuid
        self.user_id = user_id
        self.nationalCode = nationalCode
        self.gender = gender
        self.birth = birth
        self.lastLogin = lastLogin
        self.created_at = created_at
        self.updated_at = updated_at
