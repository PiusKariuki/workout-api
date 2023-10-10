from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class Movement(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("name", name="unique_name_constraint"),
    )

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(index=True)
    video: Optional[str] = None
