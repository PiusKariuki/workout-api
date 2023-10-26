from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette import status
from ..Controllers import create_workout_controller, get_all_my_workouts_controller, get_todays_workout, get_workout_by_id, \
    update_workout_controller
from ..Database import WorkoutRead, WorkoutCreate, get_db, WorkoutUpdate
from ..Services import get_current_user

workout_router = APIRouter()


@workout_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_workout(workout: WorkoutCreate, db_session: Session = Depends(get_db),
                         current_user: dict = Depends(get_current_user)) -> WorkoutRead:
    """Create a workout """
    return create_workout_controller(workout=workout, session=db_session, current_user=current_user)


@workout_router.get("/", status_code=status.HTTP_200_OK)
async def all_my_workouts(limit: int, offset: int, db_session: Session = Depends(get_db),
                       current_user: dict = Depends(get_current_user)) -> List[WorkoutRead]:
    """Get all workouts"""
    return get_all_my_workouts_controller(session=db_session, limit=limit, offset=offset, current_user=current_user)


@workout_router.get("/today", status_code=status.HTTP_200_OK)
async def today(db_session: Session = Depends(get_db)) -> WorkoutRead:
    """get today's workout"""
    return get_todays_workout(session=db_session)


@workout_router.get("/{workout_id}", status_code=status.HTTP_200_OK)
async def workout_by_id(workout_id: int, db_session: Session = Depends(get_db)) -> WorkoutRead:
    """Get workout by ID"""
    return get_workout_by_id(workout_id=workout_id, session=db_session)


@workout_router.put("/{workout_id}", status_code=status.HTTP_200_OK)
async def update_workout(workout_id: int, workout_data: WorkoutUpdate,
                         db_session: Session = Depends(get_db)) -> WorkoutRead:
    """Update a workout"""
    return update_workout_controller(workout_id=workout_id, workout_data=workout_data, session=db_session)
