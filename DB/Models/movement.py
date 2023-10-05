from sqlalchemy import Column, Integer, String

from DB.Models.base import TableBaseModel


class Movement(TableBaseModel):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
