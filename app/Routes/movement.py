from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from ..Controllers import create_movement_controller, get_all_movements, get_movement_by_name
from ..Database import get_db, MovementRead, MovementCreate

movement_router = APIRouter()


@movement_router.get("/", status_code=status.HTTP_200_OK)
async def all_movements(db_session: Session = Depends(get_db)) -> List[MovementRead]:
    return get_all_movements(session=db_session)


@movement_router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_name(name: str, db_session: Session = Depends(get_db)) -> List[MovementRead]:
    results = await get_movement_by_name(name=name, session=db_session)
    return results


@movement_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_movement(movement: MovementCreate, db_session: Session = Depends(get_db)) -> MovementRead:
    return create_movement_controller(movement=movement, session=db_session)
