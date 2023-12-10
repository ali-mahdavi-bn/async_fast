from __future__ import annotations

import datetime
import uuid

from sqlalchemy import String, ForeignKey, func, Boolean, UUID, Column, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from backbone.adapter.abstract_entity import BaseEntity
from backbone.infrastructure.databases.postgres_connection import Base


# class User(Base):
#     # __tablename__ = "users"
#     #
#     # password: Mapped[str] = mapped_column()
#     # id= mapped_column(Integer,primary_key=True,autoincrement=True)
#     # username: Mapped[str | None] = mapped_column(
#     #     unique=True, default=None, nullable=True
#     # )
#
#     # -------------------------------------------
#
#     __tablename__ = 'users'
#     __table_args__ = {'schema': 'account'}
#
#     updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
#     created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
#     deleted_at: Mapped[datetime.datetime] = mapped_column()
#     # type: #Mapped[int] = mapped_column(ForeignKey('enumeration.id'))
#     mobile: Mapped[str] = mapped_column(String(20))
#     # user_type = relationship("enumeration.id")
#
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), default_factory=uuid.uuid4,
#                                        unique=True)
#
#
#     first_name: Mapped[str] = mapped_column(String(100), default=None, nullable=True)
#     last_name: Mapped[str] = mapped_column(String(100), default=None, nullable=True)
#     email: Mapped[str] = mapped_column(String(100), default=None, nullable=True)
#     username: Mapped[str] = mapped_column(String(100),default="is_none", nullable=True)
#     is_active: Mapped[bool] = mapped_column(Boolean, default=False)
#
#     # Define the relationship to the Enumeration table


class UserEntity(Base, BaseEntity):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'account'}

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    username = Column(String(100), nullable=False)
    mobile = Column(String(20), nullable=False)
    password = Column(String(225), nullable=False)
    email = Column(String(100), nullable=True)
    type = Column(Integer, ForeignKey('enumeration.id'), nullable=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def create(self, first_name=None, last_name=None, username=None, password=None, mobile=None, email=None, type=1,
               is_active=None):
        user = UserEntity()
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.mobile = str(mobile)
        user.password = password
        user.email = email
        user.type = type
        user.is_active = is_active

        return user
