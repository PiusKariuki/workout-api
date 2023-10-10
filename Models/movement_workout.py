from typing import Optional
from sqlmodel import SQLModel, Field


class MovementWorkoutJunction(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    position: int
    movement_id: Optional[int] = Field(foreign_key="movement.id", default=None, index=True)
    workout_id: Optional[int] = Field(foreign_key="workout.id", default=None, index=True)
    sets: int
    reps: int
    rest_in_seconds: int
