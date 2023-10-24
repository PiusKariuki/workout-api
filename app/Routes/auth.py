from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from app.Controllers import create_user_controller, login_controller, recover_password_controller
from app.Database import get_db, UserCreate, AuthRead

auth_router = APIRouter()


@auth_router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
          db_session: Annotated[Session, Depends(get_db)]) -> AuthRead:
    return login_controller(form_data=form_data, session=db_session)


@auth_router.post("/register")
def register(user: UserCreate, db_session: Annotated[Session, Depends(get_db)]) -> AuthRead:
    return create_user_controller(user=user, session=db_session)


@auth_router.post("/recover")
def recover(user: UserCreate, db_session: Annotated[Session, Depends(get_db)]) -> AuthRead:
    return recover_password_controller(user=user, session=db_session)
