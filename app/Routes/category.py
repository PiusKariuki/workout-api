from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from starlette import status
from ..Controllers import create_category_controller, get_all_categories
from ..Database import get_db
from ..Database import CategoryRead, CategoryCreate

category_router = APIRouter()


@category_router.get("/", status_code=status.HTTP_200_OK)
async def all_categories(db_session: session = Depends(get_db)) -> List[CategoryRead]:
    return get_all_categories(session=db_session)


@category_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate, db_session: session = Depends(get_db)) -> CategoryRead:
    category = create_category_controller(category=category, session=db_session)
    return category
