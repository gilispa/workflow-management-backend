from pydantic import BaseModel
from typing import Optional
from app.models.task import TaskStatus
from enum import Enum


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to_id: Optional[int] = None



class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    assigned_to_id: Optional[int] = None

    class Config:
        from_attributes = True


class TaskUpdateStatus(BaseModel):
    status: TaskStatus

class TaskFilter(BaseModel):
    status: Optional[TaskStatus] = None
    assigned_to: Optional[str] = None