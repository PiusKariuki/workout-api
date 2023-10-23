from datetime import datetime
from typing import List

from sqlmodel import SQLModel


class CategoryCreate(SQLModel):
    title: str
    banner: str


class CategoryRead(CategoryCreate):
    id: int


class MovementCreate(SQLModel):
    name: str
    video: str | None = None


class MovementRead(MovementCreate):
    id: int


class MovementWorkoutJoin(SQLModel):
    movement_id: int
    movement: MovementRead | None = None
    complete: bool | None = False
    position: int
    sets: int
    reps: int
    rest_in_seconds: int | None = None


class WorkoutCreate(SQLModel):
    category_id: int
    date: datetime
    movements: List[MovementWorkoutJoin]


class WorkoutRead(SQLModel):
    id: int
    date: datetime
    category_id: int
    category: CategoryRead
    movement_links: List[MovementWorkoutJoin]


class WorkoutUpdate(SQLModel):
    date: datetime | None = None
    category_id: int | None = None


class MovementUpdate(SQLModel):
    completed: bool | None = None
    new_workout_id: int | None = None
    sets: int | None = None
    reps: int | None = None
    position: int | None = None
    rest_in_seconds: int | None = None


class UserCreate(SQLModel):
    username: str
    password: str


class AuthRead(SQLModel):
    token: str
