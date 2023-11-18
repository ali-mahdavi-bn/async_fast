from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from backbone.adapter.abstract_entity import BaseEntity
from backbone.infrastructure.databases.postgres_connection import Base


class Enumeration(Base, BaseEntity):
    __tablename__ = 'enumeration'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    parent_id = Column(Integer, ForeignKey('enumeration.id'))

    # Define the relationship to the parent enumeration if needed
    parent = relationship("Enumeration")
