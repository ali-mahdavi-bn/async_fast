from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, Boolean

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'product'}

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=True)
    title_en = Column(String(100), nullable=True)
    subset = Column(Integer, ForeignKey('product.categories.id'))
    slug = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())

    # Define the relationship to the subset category if needed
    # subset_category = relationship("Category", remote_side=[id])
