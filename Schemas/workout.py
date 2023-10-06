from datetime import date
from typing import List

from pydantic import BaseModel


class Movement(BaseModel):
    movement_id: int
    sets: int
    reps: int
    seconds_of_rest: int | None = None


class CreateWorkout(BaseModel):
    category_id: int
    date: date
    movements: List[Movement]


class ReturnWorkout(BaseModel):
    id: int
    category_id: int
    date: date
    movements: list[Movement]
