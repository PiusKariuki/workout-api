from sqlalchemy.orm import Session
from DB.Models.workout_model import Workout
from Schemas.workout import CreateWorkout


def create_workout_controller(workout: CreateWorkout, db: Session):
    workout = Workout(
        category_id=workout.category_id,
        date=workout.date
    )
    db.add(workout)
    db.commit()
    db.refresh()
    return workout
