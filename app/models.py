from pydantic import BaseModel, Field # Pydantic handles input validation
from enum import Enum # Set symbolic names bound to unique values
from typing import Optional # Let us use Optional parameter types

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Task(BaseModel): 
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str| None = Field(default=None, min_length=1, max_length=300)

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, min_length=1, max_length=300)
    status: TaskStatus | None = None
