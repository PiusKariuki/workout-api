from sqlalchemy import Column, Integer, String
from DB.Models.base import TableBaseModel


class Category(TableBaseModel):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
