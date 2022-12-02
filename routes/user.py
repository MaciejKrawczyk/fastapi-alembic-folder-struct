import fastapi
from fastapi import Path, Query
from typing import List
from schemas.user import User


router = fastapi.APIRouter()

users = []


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the user you want to retrieve", gt=2),
                   q: str = Query(None, max_length=5)):
    return [users[id], q]