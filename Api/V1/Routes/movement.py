from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from Api.V1.Controllers.movement import create_movement_controller, get_all_movements, get_movement_by_name
from Database import get_db
from Schemas.movement import CreateMovement, ReturnMovement

movement_router = APIRouter()


@movement_router.get("/", status_code=status.HTTP_200_OK)
async def all_movements(db_session: Session = Depends(get_db)) -> list[ReturnMovement]:
    return get_all_movements(session=db_session)


@movement_router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_name(name: str, db_session: Session = Depends(get_db)):
    results = await get_movement_by_name(name=name, session=db_session)
    return results


@movement_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_movement(movement: CreateMovement, db_session: Session = Depends(get_db)) -> ReturnMovement:
    return create_movement_controller(movement=movement, session=db_session)
