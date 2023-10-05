from datetime import date
from pydantic import BaseModel, Field


class CreateWorkout(BaseModel):
    category_id: int = Field(...)
    date: date = Field(...)
    exercise_id: int = Field(...)
    sets: int = Field(...)
    reps: int = Field(...)
    seconds_of_rest: int = Field(...)


