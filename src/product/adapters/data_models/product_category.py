from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, Boolean

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    __table_args__ = {'schema': 'product'}

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey('product.categories.id'))
    category_id = Column(Integer, ForeignKey('product.products.id'))

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())

    # Define the relationship to the subset category if needed
    # subset_category = relationship("Category", remote_side=[id])
