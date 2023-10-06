from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from starlette import status
from Api.V1.Controllers.workout import create_workout_controller, get_all_workouts
from DB.session import get_db
from Schemas.workout import CreateWorkout, ReturnWorkout

workout_router = APIRouter()


@workout_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_workout(workout: CreateWorkout, db: session = Depends(get_db)):
    create_workout_controller(workout=workout, db=db)


@workout_router.get("/", status_code=status.HTTP_200_OK)
async def all_workouts(db: session = Depends(get_db)):
    return get_all_workouts(db=db)
