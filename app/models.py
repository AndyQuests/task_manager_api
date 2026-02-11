from pydantic import BaseModel, Field # Pydantic handles input validation
from enum import Enum # Set symbolic names bound to unique values
from typing import Optional # Let us use Optional parameter types

class TaskStatus(str, Enum):
    """Represents the lifecycle state of a task"""
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Task(BaseModel): 
    id: int = Field(description = "Unique ID generated dynamically")
    title: str = Field(description= "Short human-readable task title")
    description: Optional[str] = Field(
        default=None, 
        description = "Optional details describing the task"
        )
    status: TaskStatus = Field(
        default=TaskStatus.pending,
        description = "Current state in the task lifecycle"
        )

class TaskCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=100,
        description= "Short human-readable title for the task"
        )
    description: str| None = Field(
        default=None,
        min_length=1,
        max_length=300,
        description="Optional details describing the task"
        )

class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="New title for the task"
        )
    description: str | None = Field(
        default=None,
        min_length=1,
        max_length=300,
        description="Updated task details")
    status: TaskStatus | None = Field(
        default=None,
        description="Updated state in the task lifecycle"
    )
