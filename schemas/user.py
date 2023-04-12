from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    upadted_at: datetime

    class Config:
        orm_mode = True
