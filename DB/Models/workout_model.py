from sqlalchemy import Integer, Column, ForeignKey, Date
from DB.Models.base_model import TableBaseModel


class Workout(TableBaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("category"), nullable=False)
    date = Column(Date, nullable=False)
