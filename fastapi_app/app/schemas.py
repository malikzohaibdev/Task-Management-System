from pydantic import BaseModel
from typing import Optional
from datetime import date

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    priority: str
    status: str

class TaskResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
