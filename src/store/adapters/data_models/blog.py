from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, Text, Boolean, UUID

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


class BlogEntity(Base):
    __tablename__ = 'blogs'
    __table_args__ = {'schema': 'store'}

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID, unique=True)
    user_id = Column(UUID, ForeignKey('account.users.uuid'))
    title = Column(String(50), nullable=True)
    title_en = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    short_description = Column(String(255), nullable=True)
    slug = Column(String(255))
    is_active = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())
    deleted_at = Column(DateTime)

    # Define relationships if needed
    # user = relationship("User")