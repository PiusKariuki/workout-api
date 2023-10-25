from fastapi import HTTPException
from sqlmodel import select, col, Session
from ..Database import Movement, MovementWorkoutJunction, MovementUpdate


def create_movement_controller(movement, session):
    try:
        new_movement = Movement(name=movement.name, video=movement.video)
        session.add(new_movement)
        session.commit()
        session.refresh(new_movement)
        return new_movement
    except Exception as e:
        print(f'\n error {e} \n')
        raise HTTPException(status_code=422)


def get_all_movements(session):
    try:
        movements = session.exec(select(Movement)).all()
        return movements
    except Exception:
        raise HTTPException(status_code=404)


async def get_movement_by_name(name, session):
    movements = session.exec(select(Movement).where(col(Movement.name).ilike(f"%{name}%"))).all()
    return movements


def update_movement_in_workout_controller(workout_id: int, movement_id: int, movement_data: MovementUpdate,
                                          session: Session):
    """updates a movement inside a workout"""
    try:
        movement = session.query(MovementWorkoutJunction).filter_by(workout_id=workout_id,
                                                                    movement_id=movement_id).one()
        if movement:
            movement.sets = movement_data.sets
            movement.reps = movement_data.reps
            movement.rest_in_seconds = movement_data.rest_in_seconds
            movement.position = movement_data.position
            movement.complete = movement_data.completed

            if movement_data.new_workout_id:
                movement.movement_id = movement_data.new_workout_id

            session.add(movement)
            session.commit()

    except Exception:
        raise HTTPException(status_code=422)


def add_movement_to_workout(workout_id: int, movement_data: MovementUpdate, session: Session):
    try:
        new_object = MovementWorkoutJunction(
            position=movement_data.position,
            workout_id=workout_id,
            movement_id=movement_data.new_workout_id,
            sets=movement_data.sets,
            reps=movement_data.reps,
            rest_in_seconds=movement_data.rest_in_seconds
        )

        session.add(new_object)
        session.commit()
        return new_object
    except Exception as e:
        print(f'\n {e.code}')
        if e.code == 'gkpj':
            raise HTTPException(status_code=409, detail='This movement already exists in this workout')
        raise HTTPException(status_code=422)


def delete_split(workout_id: int, movement_id: int, session: Session):
    try:
        split = session.query(MovementWorkoutJunction).filter_by(workout_id=workout_id,
                                                                 movement_id=movement_id).one()
        session.delete(split)
        session.commit()
    except Exception:
        raise HTTPException(status_code=422)
