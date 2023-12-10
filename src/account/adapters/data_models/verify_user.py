from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, UUID
from sqlalchemy.orm import relationship

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


class VerifyUser(Base):
    __tablename__ = 'verify_users'
    __table_args__ = {'schema': 'account'}

    id = Column(Integer, primary_key=True)
    mobile = Column(String(20))
    code = Column(String(10))
    user_id = Column(UUID(as_uuid=True), ForeignKey('account.users.uuid'))
    mode = Column(Integer, ForeignKey('enumeration.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Define the relationship to the Enumeration table for mode if needed
    verify_mode = relationship("Enumeration", foreign_keys=[mode])
    # Define the relationship to the User table
    user = relationship("User")
