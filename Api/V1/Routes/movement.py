from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from Api.V1.Controllers.movement import create_movement_controller
from DB.session import get_db
from Schemas.movement import CreateMovement, ReturnMovement

movement_router = APIRouter()


@movement_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_movement(movement: CreateMovement, db: Session = Depends(get_db)) -> ReturnMovement:
    new_movement = create_movement_controller(movement=movement, db=db)
    return new_movement
