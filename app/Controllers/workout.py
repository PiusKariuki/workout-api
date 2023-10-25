from datetime import date, datetime, time
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select, Session
from ..Database import MovementWorkoutJunction
from ..Database import Workout


def create_workout_controller(workout, session, current_user):
    """Creates a workout with a date and category and includes movements in the junction table"""
    try:
        # set the time to midnight
        new_date = datetime.combine(workout.date, time.min)

        new_workout = Workout(category_id=workout.category_id, date=new_date, user_id=current_user.id)

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

        return new_workout

    except IntegrityError:
        raise HTTPException(status_code=409, detail='A workout for this date already exists')

    except Exception:
        raise HTTPException(status_code=422)


def update_workout_controller(workout_id, workout_data, session: Session):
    """updates a workout"""
    try:
        workout = session.get(Workout, workout_id)
        if workout:
            workout.date = workout_data.date
            workout.category_id = workout_data.category_id
            session.add(workout)
            session.commit()
        return workout
    except Exception:
        raise HTTPException(status_code=422)


def get_todays_workout(session):
    """Get the workout of the day """
    try:
        # get the year month and date in string format
        date_today = date.today().strftime('%Y-%m-%d')
        # get the one record with that date
        todays_workout = session.exec(select(Workout).where(Workout.date == date_today)).one()
        return todays_workout
    except Exception:
        raise HTTPException(status_code=404)


def get_all_workouts(session, limit, offset):
    try:
        return (session
                .exec(select(Workout).limit(limit).offset(offset).order_by(Workout.date.desc()))
                .all())
    except Exception as e:
        print(f'\n error {e} \n')
        raise HTTPException(status_code=404)


def get_workout_by_id(session, workout_id):
    try:
        return session.get(Workout, workout_id)
    except Exception:
        raise HTTPException(status_code=404)
