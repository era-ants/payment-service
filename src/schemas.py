"""
Module: schemas.py
Author: vgolubev

Module describe pydantic schemas for requests and responses.  
"""

from typing import List, Optional
from pydantic import BaseModel


class Money(BaseModel):
    client_id: int
    digits: float
    currency: str


class Payment(Money):
    pass
