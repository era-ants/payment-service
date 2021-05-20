"""
Module: schemas.py
Author: vgolubev

Module describe pydantic schemas for requests and responses.  
"""

from typing import List, Optional
from pydantic import BaseModel


class HelloMessage(BaseModel):
    message: str

class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id:int

    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True