from unittest.mock import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

import owner

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'))

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    breed = Column(String)
    temperament = Column(String)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    