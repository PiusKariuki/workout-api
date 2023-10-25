from datetime import datetime
from typing import Optional, List
from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("username", name="unique_username_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    username: str
    password: str
    workouts: List["Workout"] = Relationship(back_populates="user")
    role_links: List["UserRoles"] = Relationship(back_populates="user")


class Roles(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    description: str | None = None
    user_links: List["UserRoles"] = Relationship(back_populates="role")


class UserRoles(SQLModel, table=True):
    user_id: Optional[int] = Field(foreign_key="user.id", default=None, index=True, primary_key=True)
    role_id: Optional[int] = Field(foreign_key="roles.id", default=None, index=True, primary_key=True)
    user: "User" = Relationship(back_populates="role_links")
    role: "Roles" = Relationship(back_populates="user_links")


class Category(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("title", name="unique_title_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    title: str = Field(index=True)
    banner: str
    # relationships attributes
    workouts: List["Workout"] = Relationship(back_populates="category")


class MovementWorkoutJunction(SQLModel, table=True):
    position: int
    movement_id: Optional[int] = Field(foreign_key="movement.id", default=None, index=True, primary_key=True)
    workout_id: Optional[int] = Field(foreign_key="workout.id", default=None, index=True, primary_key=True)
    complete: Optional[bool] = False
    sets: int
    reps: int
    rest_in_seconds: int
    # relationship attributes
    movement: "Movement" = Relationship(back_populates="workout_links")
    workout: "Workout" = Relationship(back_populates="movement_links")


class Movement(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("name", name="unique_name_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(index=True)
    video: Optional[str] = None
    # relationship attributes
    workout_links: List["MovementWorkoutJunction"] = Relationship(back_populates="movement")


class Workout(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("date", name="unique_date_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    category_id: Optional[int] = Field(foreign_key="category.id", default=None)
    user_id: Optional[int] = Field(foreign_key="user.id", default=None)
    date: datetime = Field(index=True)
    # relationship attributes
    category: Category = Relationship(back_populates="workouts")
    movement_links: List["MovementWorkoutJunction"] = Relationship(back_populates="workout")
    user: "User" = Relationship(back_populates="workouts")
