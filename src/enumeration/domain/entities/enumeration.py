from backbone.adapter.abstract_entity import BaseEntity


class Enumeration(BaseEntity):
    id: int
    title: str
    parent_id: int

    def __init__(self, id=None, title=None, parent_id=None):
        self.id = id
        self.title = title
        self.parent_id = parent_id
