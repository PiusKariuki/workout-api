from sqlmodel import Session, select
from Database import Category
from Schemas import CreateCategory


def create_category_controller(category: CreateCategory, session: Session):
    category = Category(title=category.title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_all_categories(session: Session):
    categories = session.exec(select(Category)).all()
    return categories
