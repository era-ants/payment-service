"""
Module: models.py
Author: vgolubev

Module describe orm models in application.  
"""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# change this models for yours

class Money(Base):
    __tablename__ = 'Money'

    id = Column(Integer, primary_key=True)
    digits = Column(Float)
    currency = Column(String(10))
