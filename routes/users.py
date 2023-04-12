import fastapi
from fastapi import Path, Query, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from schemas.user import UserCreate, User
from routes.utils.users import get_user, get_users, get_user_by_email, create_user
from config.database import get_db

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users")
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


