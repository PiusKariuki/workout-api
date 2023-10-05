from sqlalchemy import Column, Integer, String

from DB.Models.base_model import TableBaseModel


class VideoLink(TableBaseModel):
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)