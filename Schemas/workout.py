from datetime import date
from typing import List
from pydantic import BaseModel


class Movement(BaseModel):
    movement_id: int
    position: int
    sets: int
    reps: int
    rest_in_seconds: int | None = None


class CreateWorkout(BaseModel):
    category_id: int
    date: date
    movements: List[Movement]


class ReturnWorkout(BaseModel):
    success: bool
