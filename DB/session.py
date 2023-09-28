from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Core.config import settings

print(f'Database URI is {settings.DATABASE_URI}')

engine = create_engine(settings.DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
