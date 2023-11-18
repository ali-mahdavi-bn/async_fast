import datetime
from uuid import UUID

from backbone.adapter.abstract_entity import BaseEntity


class productEntity(BaseEntity):
    id: int
    uuid: UUID
    title: str
    title_en: str
    short_description: str
    description: str
    category_id: int
    store_id: int
    slug: str
    showOnHomepage: bool
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime

    def __init__(self
                 , id
                 , uuid
                 , title
                 , title_en
                 , short_description
                 , description
                 , category_id
                 , store_id
                 , slug
                 , showOnHomepage
                 , is_active
                 , created_at
                 , updated_at
                 , deleted_at
                 ):
        self.id = id
        self.uuid = uuid
        self.title = title
        self.title_en = title_en
        self.short_description = short_description
        self.description = description
        self.category_id = category_id
        self.store_id = store_id
        self.slug = slug
        self.showOnHomepage = showOnHomepage
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
