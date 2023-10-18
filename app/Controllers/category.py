from sqlmodel import select
from app.Database import Category


def create_category_controller(category, session):
    category = Category(title=category.title, banner=category.banner)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_all_categories(session):
    categories = session.exec(select(Category)).all()
    return categories
