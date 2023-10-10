from typing import Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("title", name="unique_title_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    title: str = Field(index=True)
