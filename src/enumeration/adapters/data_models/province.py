from sqlalchemy import Integer, Column, String

from backbone.infrastructure.databases.postgres_connection import Base


class Province(Base):
    __tablename__ = 'provinces'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    slug = Column(String(100))
