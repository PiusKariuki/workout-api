from sqlalchemy import Column, Integer, ForeignKey

from DB.Models.base_model import BaseModel


class ExerciseMovement(BaseModel):
    id = Column(Integer, primary_key=True)
    movement_id = Column(Integer, ForeignKey("movement"), nullable=False)
    workout_id = Column(Integer, ForeignKey("workout"), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer)
    rest_in_seconds = Column(Integer)
