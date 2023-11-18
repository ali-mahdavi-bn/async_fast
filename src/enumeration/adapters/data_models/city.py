from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from backbone.infrastructure.databases.postgres_connection import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    slug = Column(String(100))
    province_id = Column(Integer, ForeignKey('provinces.id'))

    # Define the relationship to the Province table
    province = relationship("Province")
