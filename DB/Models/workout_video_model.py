from sqlalchemy import Column, Integer, ForeignKey

from DB.Models.base_model import BaseModel


class WorkoutVideoModel(BaseModel):
    id = Column(Integer, primary_key=True)
    video_link_id = Column(Integer, ForeignKey=True)
    workout_id = Column(Integer, ForeignKey=True)