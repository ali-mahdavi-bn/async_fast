from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime, UUID

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import Base


# class UserDetails(Base):
#     __tablename__ = 'user_details'
#     __table_args__ = {'schema': 'account'}
#
#     id = Column(Integer, primary_key=True)
#     uuid = Column(UUID(as_uuid=True), unique=True)
#     user_id = Column(UUID(as_uuid=True), ForeignKey('account.users.uuid'))
#     nationalCode = Column(String(10), nullable=True)
#     gender = Column(Integer, ForeignKey('enumeration.id'))
#     birth = Column(DateTime, nullable=True)
#     lastLogin = Column(DateTime, nullable=True)
#     created_at = Column(DateTime, server_default=func.now())
#     updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Define the relationship to the Enumeration table for gender if needed
    # user_gender = relationship("Enumeration", foreign_keys=[gender])
    # Define the relationship to the User table
    # use