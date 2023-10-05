from sqlalchemy.orm import Session

from DB.Models.category_model import Category
from Schemas.category import CreateCategory


def create_category_controller(category: CreateCategory, db: Session):
    category = Category(
        title=category.title
    )


    db.add(category)
    db.commit()
    return category
