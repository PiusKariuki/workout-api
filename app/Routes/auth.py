from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.Controllers import create_user_controller
from app.Database import get_db, UserCreate, AuthRead

auth_router = APIRouter()


@auth_router.post("/register")
def register(user: UserCreate, db_session: Annotated[Session, Depends(get_db)]) -> AuthRead:
    return create_user_controller(user=user, session=db_session)
