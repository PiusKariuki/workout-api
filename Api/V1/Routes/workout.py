from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette import status
from Api.V1.Controllers.workout import create_workout_controller, get_all_workouts, get_todays_workout
from Database import get_db
from Schemas.workout import CreateWorkout, ReturnWorkout

workout_router = APIRouter()


@workout_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_workout(workout: CreateWorkout, db_session: Session = Depends(get_db)) -> ReturnWorkout:
    return create_workout_controller(workout=workout, session=db_session)


@workout_router.get("/", status_code=status.HTTP_200_OK)
async def all_workouts(db_session: Session = Depends(get_db)):
    return get_all_workouts(session=db_session)


@workout_router.get("/today", status_code=status.HTTP_200_OK)
async def today(db_session: Session = Depends(get_db)):
    return get_todays_workout(session=db_session)