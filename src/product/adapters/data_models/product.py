from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, Text, Boolean, UUID

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'product'}

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID, unique=True)
    title = Column(String(100), nullable=True)
    title_en = Column(String(100), nullable=True)
    short_description = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey('product.categories.id'))
    store_id = Column(UUID, ForeignKey('store.stores.uuid'))
    slug = Column(String(255), nullable=True)
    showOnHomepage = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())
    deleted_at = Column(DateTime)

    # Define relationships if needed
    # category = relationship("Category")
    # store = relationship("Store")
