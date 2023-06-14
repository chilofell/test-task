from uuid import UUID
from pydantic import BaseModel


class Params(BaseModel):
    param_1: str
    param_2: int


# модель изменения
class TaskBase(BaseModel):
    uuid: UUID
    description: str
    params: Params


class Task(TaskBase):
    id: int

