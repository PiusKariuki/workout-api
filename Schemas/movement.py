from pydantic import BaseModel


class CreateMovement(BaseModel):
    name: str
    video: str


class ReturnMovement(BaseModel):
    id: int
    name: str
    video: str
