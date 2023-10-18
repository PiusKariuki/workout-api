from typing import Generator

from sqlmodel import create_engine, Session

from ..Core.config import settings


engine = create_engine(settings.DATABASE_URI, echo=True)


def get_db() -> Generator:
    try:
        db = Session(engine)
        yield db
    finally:
        db.close()
