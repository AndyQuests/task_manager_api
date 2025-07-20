from fastapi import FastAPI, Path
from fastapi import HTTPException # Let us return proper status codes (e.g. 404)
from pydantic import BaseModel  # Pydantic handles input validation
from typing import Optional, List # Let us use Optional, List parameter types
from enum import Enum # Set symbolic names bound to unique values

app = FastAPI()

# In-memory task storage
tasks = []

# Task Status Model
class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

# Task Data Model
class Task(BaseModel): 
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    status: TaskStatus = TaskStatus.pending

# Welcome route :)
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Get all tasks
@ app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

# Fetch a single task by ID
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int): 
    for task in tasks: 
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Create a new task
@app.post("/tasks")
async def create_task(task: Task):
    tasks.append(task)
    return task

# Add PATCH endpoint to update a task's status
@app.patch("/tasks/{task_id}/status")
async def update_task_status(task_id:int, status: TaskStatus):
    for task in tasks:
        if task.id == task_id:
            task.status = status
            return task
    raise HTTPException(status_code=404, detail= "Task not found")
