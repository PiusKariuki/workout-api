from pydantic import BaseModel


class CreateMovement(BaseModel):
    name: str
    video: str


class ReturnMovement(CreateMovement):
    id: int
