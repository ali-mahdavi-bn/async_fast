from __future__ import annotations

from backbone.adapter.abstract_entity import BaseEntity


class City(BaseEntity):
    id: int
    name: str
    slug: str
    province_id: int

    def __init__(self, id: int,
                 name: str,
                 slug: str, province_id: int):
        self.id = id
        self.name = name
        self.slug = slug
        self.province_id = province_id
