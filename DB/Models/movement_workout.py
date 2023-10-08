from sqlalchemy import Column, Integer, ForeignKey

from DB.Models.base import TableBaseModel


class MovementWorkoutJunction(TableBaseModel):
    id = Column(Integer, primary_key=True)
    position = Column(Integer, nullable=False)
    movement_id = Column(Integer, ForeignKey("movement.id"), nullable=False)
    workout_id = Column(Integer, ForeignKey("workout.id"), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer)
    rest_in_seconds = Column(Integer)
