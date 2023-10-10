from typing import Generator
from sqlalchemy import create_engine
from sqlmodel import Session
from Core.config import settings

# table imports imports
from .movement import Movement
from .category import Category
from .movement_workout import MovementWorkoutJunction
from .workout import Workout

engine = create_engine(settings.DATABASE_URI, echo=True)


def get_db() -> Generator:
    try:
        db = Session(engine)
        yield db
    finally:
        db.close()
