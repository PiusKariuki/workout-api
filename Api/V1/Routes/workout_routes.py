from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from starlette import status
from Api.V1.Controllers.workout_controller import create_workout_controller
from DB.session import get_db
from Schemas.workout import CreateWorkout, ReturnWorkout

workout_router = APIRouter()


@workout_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_workout(workout: CreateWorkout, db: session = Depends(get_db)) -> ReturnWorkout:
    workout = create_workout_controller(workout=workout, db=db)
    return workout
