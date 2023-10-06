import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.sql import cast
from DB.Models.category import Category
from DB.Models.movement_workout import MovementWorkoutJunction
from DB.Models.workout import Workout
from Schemas.workout import CreateWorkout


def create_workout_controller(workout: CreateWorkout, db: Session):
    new_workout = Workout(
        category_id=workout.category_id,
        date=workout.date
    )

    db.add(new_workout)
    db.flush()

    saved_movements = []
    for movement in workout.movements:
        new_movement = MovementWorkoutJunction(
            movement_id=movement.movement_id,
            workout_id=new_workout.id,
            sets=movement.sets,
            reps=movement.reps,
            rest_in_seconds=movement.seconds_of_rest
        )
        db.add(new_movement)
        db.commit()
        saved_movements.append(new_movement)

    db.commit()


def get_all_workouts(db: Session):
    workouts = db.query(
        Workout.id,
        Workout.date,
        Category.title
    ).join(Category, cast(Workout.category_id, sqlalchemy.Integer) == Category.id).all()

    workouts = [{
        "id":row.id,
        "date":row.date,
        "category_title":row.title,
    } for row in workouts]

    return workouts

