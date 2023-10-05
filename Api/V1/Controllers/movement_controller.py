from sqlalchemy.orm import Session

from DB.Models.movement_model import Movement
from Schemas.movement import CreateMovement


def create_movement_controller(movement: CreateMovement, db: Session):
    new_movement = Movement(
        name=movement.name
    )
    db.add(new_movement)
    db.commit()

    return  new_movement
