from __future__ import annotations

from backbone.adapter.abstract_entity import BaseEntity


class Province(BaseEntity):
    id: int
    name: str
    slug: str

    def __init__(self, id: int,
                 name: str,
                 slug: str):
        self.id = id
        self.name = name
        self.slug = slug
