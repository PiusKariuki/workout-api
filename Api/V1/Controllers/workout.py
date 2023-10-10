from datetime import datetime, date
from fastapi import HTTPException
from sqlmodel import Session, Integer, cast, select, col
from Models import Category
from Models import MovementWorkoutJunction
from Models import Workout
from Schemas import CreateWorkout


def create_workout_controller(workout: CreateWorkout, session: Session):
    try:
        # convert date string to datetime object
        date_format = '%Y-%m-%d'
        datetime_object = datetime.strptime(str(workout.date), date_format)

        new_workout = Workout(category_id=workout.category_id, date=datetime_object)

        session.add(new_workout)
        session.commit()
        session.refresh(new_workout)

        movement_mappings = []
        for movement in workout.movements:
            new_movement = MovementWorkoutJunction(
                movement_id=movement.movement_id,
                workout_id=new_workout.id,
                position=movement.position,
                sets=movement.sets,
                reps=movement.reps,
                rest_in_seconds=movement.rest_in_seconds
            )
            movement_mappings.append(new_movement)

        session.add_all(movement_mappings)
        session.commit()

        return {"success": True}

    except Exception:
        raise HTTPException(status_code=422)


def get_todays_workout(session: Session):
    try:
        # get the year month and date in string format
        date_today = date.today().strftime('%Y-%m-%d')
        # get the one record with that date
        todays_workout = session.exec(select(Workout).where(Workout.date == date_today)).one()
        return todays_workout
    except Exception:
        raise HTTPException(status_code=404)


def get_all_workouts(session: Session):
    workouts = session.query(
        Workout.id,
        Workout.date,
        Category.title
    ).join(Category, cast(Workout.category_id, Integer) == Category.id).all()

    workouts = [{
        "id": row.id,
        "date": row.date,
        "category_title": row.title,
    } for row in workouts]

    return workouts
