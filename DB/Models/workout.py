from sqlalchemy import Integer, Column, ForeignKey, Date
from DB.Models.base import TableBaseModel


class Workout(TableBaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    date = Column(Date, nullable=False)
