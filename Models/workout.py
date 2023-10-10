from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, UniqueConstraint


class Workout(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("date", name="unique_date_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    category_id: Optional[int] = Field(foreign_key="category.id", default=None)
    date: datetime = Field(index=True)
