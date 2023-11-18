from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, UUID

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


class ClickHistory(Base):
    __tablename__ = 'click_histories'
    __table_args__ = {'schema': 'product'}

    id = Column(Integer, primary_key=True)
    userAgent = Column(Integer, ForeignKey('enumeration.id'))
    store_id = Column(UUID, ForeignKey('store.stores.uuid'))
    product_id = Column(UUID, ForeignKey('product.products.uuid'))
    ipv4 = Column(String(20))
    ipv6 = Column(String(40))
    device_id = Column(String(20))
    created_at = Column(DateTime, default=func.now())
    deleted_at = Column(DateTime)

    # Define relationships if needed
    # user_agent = relationship("Enumeration")
    # store = relationship("Store")
    # product = relationship("Product")
