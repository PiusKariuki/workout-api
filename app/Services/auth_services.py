from datetime import datetime, timedelta
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.hash import bcrypt
from fastapi import HTTPException, Depends

from sqlmodel import Session, select

from app.Core import settings
from app.Database import User, get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Annotated[Session, Depends(get_db)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="username field empty")

        user = session.exec(select(User).where(User.username == username)).one()

        if user is None:
            raise HTTPException(status_code=404, detail="User does not exist in the database")
        return user

    except Exception:
        raise HTTPException(status_code=401, detail="Not authenticated")


def hash_password(password: str):
    return bcrypt.hash(password)


def verify_password(password: str, hashed_password: str):
    return bcrypt.verify(password, hashed_password)
