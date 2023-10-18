from fastapi import APIRouter
from app.Routes.category import category_router
from app.Routes.movement import movement_router
from app.Routes.workout import workout_router

index_router = APIRouter()

index_router.include_router(workout_router, prefix="/workouts", tags=['Workout'])

index_router.include_router(category_router, prefix='/category', tags=['category'])

index_router.include_router(movement_router, prefix='/movement', tags=['movement'])
