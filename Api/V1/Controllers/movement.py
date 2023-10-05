from sqlalchemy.orm import Session

from DB.Models.movement import Movement
from Schemas.movement import CreateMovement


def create_movement_controller(movement: CreateMovement, db: Session):
    new_movement = Movement(name=movement.name,video=movement.video)
    db.add(new_movement)
    db.commit()

    return new_movement
