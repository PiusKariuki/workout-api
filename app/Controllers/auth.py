from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from jose import JWTError, jwt
from sqlmodel import Session
from passlib.context import CryptContext
from starlette import status
from app.Core import settings
from app.Database import UserCreate, User

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def create_access_token(data:dict):
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


def get_current_user(token: str = Depends(decode_token)):
    if token:
        return token
    else:
        raise HTTPException(status_code=401, detail="Not authenticated")


def hash_password(password: str):
    return pwd_context.hash(password)


def create_user_controller(user: UserCreate, session: Session):
    """Controller to create user"""
    try:
        new_user = User(username=user.username, password=hash_password(user.password))
        session.add(new_user)
        session.commit()

        token = create_access_token({"sub": new_user.username})
        return {"id": new_user.id, "token": token}

    except Exception as e:
        print(f'\n {e}\n')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
