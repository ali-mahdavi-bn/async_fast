import datetime

from backbone.adapter.abstract_entity import BaseEntity


class clickHistoryEntity(BaseEntity):
    id: int
    userAgent: str
    store_id: int
    product_id: int
    ipv4: str
    ipv6: str
    device_id: int
    created_at: datetime.datetime
    deleted_at: datetime.datetime

    def __init__(self
                 , id=None
                 , userAgent=None
                 , store_id=None
                 , product_id=None
                 , ipv4=None
                 , ipv6=None
                 , device_id=None
                 , created_at=None
                 , deleted_at=None
                 ):
        self.id = id
        self.userAgent = userAgent
        self.store_id = store_id
        self.product_id = product_id
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.device_id = device_id
        self.created_at = created_at
        self.deleted_at = deleted_at
