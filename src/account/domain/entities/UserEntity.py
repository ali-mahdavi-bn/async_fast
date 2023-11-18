import datetime
from uuid import UUID

from backbone.adapter.abstract_entity import BaseEntity


class UserEntity(BaseEntity):
    id: int
    uuid: UUID
    first_name: str
    last_name: str
    username: str
    mobile: int
    email: str
    type: int
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime

    def __init__(self
                 , id=None
                 , uuid=None
                 , first_name=None
                 , last_name=None
                 , username=None
                 , mobile=None
                 , email=None
                 , type=None
                 , is_active=None
                 , created_at=None
                 , updated_at=None
                 , deleted_at=None
                 ):
        self.id = id
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.mobile = mobile
        self.email = email
        self.type = type
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
