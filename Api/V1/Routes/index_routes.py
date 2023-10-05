from fastapi import APIRouter

from Api.V1.Routes.workout_routes import workout_router

index_router = APIRouter()

index_router.include_router(workout_router, prefix="/workouts", tags=['Workout'])
