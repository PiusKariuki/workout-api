from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette import status
from ..Controllers import create_workout_controller, get_all_workouts, get_todays_workout, get_workout_by_id
from ..Database import get_db
from ..Database import WorkoutRead, WorkoutCreate

workout_router = APIRouter()


@workout_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_workout(workout: WorkoutCreate, db_session: Session = Depends(get_db)) -> WorkoutRead:
    return create_workout_controller(workout=workout, session=db_session)


@workout_router.get("/", status_code=status.HTTP_200_OK)
async def all_workouts(limit: int, offset: int, db_session: Session = Depends(get_db)) -> List[WorkoutRead]:
    return get_all_workouts(session=db_session, limit=limit, offset=offset)


@workout_router.get("/today", status_code=status.HTTP_200_OK)
async def today(db_session: Session = Depends(get_db)) -> WorkoutRead:
    return get_todays_workout(session=db_session)


@workout_router.get("/{workout_id}", status_code=status.HTTP_200_OK)
async def workout_by_id(workout_id: int, db_session: Session = Depends(get_db)) ->WorkoutRead:
    return get_workout_by_id(workout_id=workout_id, session=db_session)
