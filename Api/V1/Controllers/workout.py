from sqlalchemy.orm import Session
from DB.Models.workout import Workout


def create_workout_controller(workout, db: Session):
    workout = Workout(
        category_id=workout.category_id,
        date=workout.date
    )
    db.add(workout)
    db.commit()
    # db.refresh(ses)
    return workout
