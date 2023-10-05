from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from starlette import status
from Api.V1.Controllers.category_controller import create_category_controller
from DB.session import get_db
from Schemas.category import CreateCategory, ReturnCategory

category_router = APIRouter()


@category_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(category: CreateCategory, db: session = Depends(get_db)) -> ReturnCategory:
    category = create_category_controller(category=category, db=db)
    return category
