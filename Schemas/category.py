from pydantic import BaseModel


class CreateCategory(BaseModel):
    title: str


class ReturnCategory(CreateCategory):
    id: int
