from fastapi import APIRouter
from .auth import auth_router
from ..Routes.category import category_router
from ..Routes.movement import movement_router
from ..Routes.workout import workout_router

index_router = APIRouter()

index_router.include_router(workout_router, prefix="/workouts", tags=['Workout'])

index_router.include_router(category_router, prefix='/category', tags=['category'])

index_router.include_router(movement_router, prefix='/movement', tags=['movement'])

index_router.include_router(auth_router, prefix='/auth', tags=['Auth'])
