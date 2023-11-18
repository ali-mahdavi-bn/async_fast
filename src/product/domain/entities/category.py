import datetime

from backbone.adapter.abstract_entity import BaseEntity


class categoryEntity(BaseEntity):
    id: int
    title: str
    title_en: str
    subset: int
    slug: str
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self
                 , id=None
                 , title=None
                 , title_en=None
                 , subset=None
                 , slug=None
                 , is_active=None
                 , created_at=None
                 , updated_at=None
                 ):
        self.id = id
        self.title = title
        self.title_en = title_en
        self.subset = subset
        self.slug = slug
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
