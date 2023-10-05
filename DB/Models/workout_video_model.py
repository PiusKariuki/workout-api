from sqlalchemy import Column, Integer, ForeignKey

from DB.Models.base_model import TableBaseModel


class MovementVideoModel(TableBaseModel):
    id = Column(Integer, primary_key=True)
    video_link_id = Column(Integer, ForeignKey=True)
    movement_id = Column(Integer, ForeignKey=True)