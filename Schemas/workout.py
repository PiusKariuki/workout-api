from datetime import date
from pydantic import BaseModel


class CreateWorkout(BaseModel):
    category_id: int
    date: date
    exercise_id: int
    sets: int
    reps: int
    seconds_of_rest: int | None = None


class ReturnWorkout(BaseModel):
    id: int
    category_id: int
    date: date
    exercise_id: int
    sets: int
    reps: int
    seconds_of_rest: int | None = None
