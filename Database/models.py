from datetime import datetime
from typing import Optional, List
from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("title", name="unique_title_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    title: str = Field(index=True)

    workouts: List["Workout"] = Relationship(back_populates="category")


class Movement(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("name", name="unique_name_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(index=True)
    video: Optional[str] = None


class MovementWorkoutJunction(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    position: int
    movement_id: Optional[int] = Field(foreign_key="movement.id", default=None, index=True)
    workout_id: Optional[int] = Field(foreign_key="workout.id", default=None, index=True)
    sets: int
    reps: int
    rest_in_seconds: int


class Workout(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("date", name="unique_date_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    category_id: Optional[int] = Field(foreign_key="category.id", default=None)
    date: datetime = Field(index=True)

    category: Category = Relationship(back_populates="workouts")
