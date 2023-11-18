from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, Text, UUID

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


class Store(Base):
    __tablename__ = 'stores'
    __table_args__ = {'schema': 'store'}

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID, unique=True)
    brand_id = Column(UUID, ForeignKey('store.brands.uuid'))
    manager_id = Column(UUID, ForeignKey('account.users.uuid'))
    title = Column(String(100), nullable=True)
    title_en = Column(String(100))
    short_description = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    slug = Column(String(255))
    address = Column(String(255))
    phone_number = Column(String(20), nullable=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=True)
    postingMethods = Column(Integer, ForeignKey('enumeration.id'), nullable=True)
    paymentMethods = Column(Integer, ForeignKey('enumeration.id'), nullable=True)
    orderTrackingMethods = Column(Integer, ForeignKey('enumeration.id'), nullable=True)
    latitude = Column(String(15), nullable=True)
    longitude = Column(String(15), nullable=True)
    status = Column(Integer, ForeignKey('enumeration.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())
    deleted_at = Column(DateTime)