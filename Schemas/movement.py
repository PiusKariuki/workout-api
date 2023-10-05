from pydantic import BaseModel


class CreateMovement(BaseModel):
    name: str


class ReturnMovement(BaseModel):
    id: int
    name: str
