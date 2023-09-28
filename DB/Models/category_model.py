from sqlalchemy import Column, Integer, String

from DB.Models.base_model import BaseModel


class Category(BaseModel):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
