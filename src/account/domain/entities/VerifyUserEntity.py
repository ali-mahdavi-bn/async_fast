import datetime
from uuid import UUID

from backbone.adapter.abstract_entity import BaseEntity


class VerifyUserEntity(BaseEntity):
    id: int
    mobile: int
    code: int
    user_id: UUID
    mode: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self,
                 id=None,
                 mobile=None,
                 code=None,
                 user_id=None,
                 mode=None,
                 created_at=None,
                 updated_at=None
                 ):
        self.id = id
        self.mobile = mobile
        self.code = code
        self.user_id = user_id
        self.mode = mode
        self.created_at = created_at
        self.updated_at = updated_at
