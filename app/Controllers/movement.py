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
    except Exception:
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

    except Exception as e:
        print(f'error ${e}')
        raise HTTPException(status_code=422)
