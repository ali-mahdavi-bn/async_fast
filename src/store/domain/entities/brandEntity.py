import datetime
from uuid import UUID

from backbone.adapter.abstract_entity import BaseEntity


class BrandEntity(BaseEntity):
    id: int
    uuid: UUID
    user_id: UUID
    title: str
    title_en: str
    description: str
    short_description: str
    slug: str
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime

    def __init__(self
                 , id=None
                 , uuid=None
                 , user_id=None
                 , title=None
                 , title_en=None
                 , description=None
                 , short_description=None
                 , slug=None
                 , is_active=None
                 , created_at=None
                 , updated_at=None
                 , deleted_at=None
                 ):
        self.id = id
        self.uuid = uuid
        self.user_id = user_id
        self.title = title
        self.title_en = title_en
        self.description = description
        self.short_description = short_description
        self.slug = slug
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
