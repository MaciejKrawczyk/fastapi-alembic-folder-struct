from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]
