from fastapi import HTTPException
from sqlmodel import Session, select, col
from Database import Movement
from Schemas.movement import CreateMovement


def create_movement_controller(movement: CreateMovement, session: Session):
    try:
        new_movement = Movement(name=movement.name, video=movement.video)
        session.add(new_movement)
        session.commit()
        session.refresh(new_movement)
        return new_movement
    except Exception:
        raise HTTPException(status_code=422)


def get_all_movements(session: Session):
    try:
        movements = session.exec(select(Movement)).all()
        return movements
    except Exception:
        raise HTTPException(status_code=404)


async def get_movement_by_name(name: str, session: Session):
    movements = session.exec(select(Movement).where(col(Movement.name).ilike(f"%{name}%"))).all()
    return movements
