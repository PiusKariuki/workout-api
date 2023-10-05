from pydantic import BaseModel


class CreateCategory(BaseModel):
    title: str


class ReturnCategory(BaseModel):
    id: int
    title: str
