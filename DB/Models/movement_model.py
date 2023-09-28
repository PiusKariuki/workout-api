from sqlalchemy import Column, Integer, String

from DB.Models.base_model import BaseModel


class Movement(BaseModel):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
