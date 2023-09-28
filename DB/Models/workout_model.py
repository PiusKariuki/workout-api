from sqlalchemy import Integer, Column, ForeignKey, Date

from DB.Models.base_model import BaseModel


class WorkoutSchema(BaseModel):
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("category"), nullable=False)
    date = Column(Date, nullable=False)
