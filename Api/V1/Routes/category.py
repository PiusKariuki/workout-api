from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from starlette import status
from Api.V1.Controllers.category import create_category_controller, get_all_categories
from DB.session import get_db
from Schemas.category import CreateCategory, ReturnCategory

category_router = APIRouter()


@category_router.get("/", status_code=status.HTTP_200_OK)
async def all_categories(db: session = Depends(get_db)) -> list[ReturnCategory]:
    return get_all_categories(db=db)


@category_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(category: CreateCategory, db: session = Depends(get_db)) -> ReturnCategory:
    category = create_category_controller(category=category, db=db)
    return category