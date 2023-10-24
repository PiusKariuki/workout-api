from fastapi import HTTPException
from sqlmodel import Session, select
from starlette import status
from app.Database import UserCreate, User
from app.Services import verify_password, create_access_token, hash_password


def login_controller(form_data, session: Session):
    """login controller"""
    try:
        user = session.exec(select(User).where(User.username == form_data.username)).one()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username")

        if not verify_password(form_data.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "Bearer"}
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def create_user_controller(user: UserCreate, session: Session):
    """Controller to create user"""
    try:
        new_user = User(username=user.username, password=hash_password(user.password))
        session.add(new_user)
        session.commit()
        token = create_access_token({"sub": new_user.username})
        return {"access_token": token, "token_type": "Bearer"}

    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def recover_password_controller(user: UserCreate, session: Session):
    try:
        user_object = session.exec(select(User).where(User.username == user.username)).one()
        if not user_object:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username")

        user_object.password = hash_password(user.password)

        session.add(user_object)
        session.commit()

        token = create_access_token({"sub": user_object.username})
        return {"access_token": token, "token_type": "Bearer"}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
