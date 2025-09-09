from fastapi import FastAPI, Path
from fastapi import HTTPException # Let us return proper status codes (e.g. 404)
from pydantic import BaseModel  # Pydantic handles input validation
from typing import Optional, List # Let us use Optional, List parameter types
from enum import Enum # Set symbolic names bound to unique values

# ---------------------
#      1. MODELS
# ---------------------

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
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    status: TaskStatus


# ---------------------
#       2. APP + STORAGE
# ---------------------

app = FastAPI()
tasks : dict[int, Task] = {}


# ---------------------
#       3. ENDPOINTS
# ---------------------

# Welcome route :)
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Get all tasks
@ app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks.values() ### < check

# Fetch a single task by ID
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int): 
    if task_id in tasks:
        return tasks[task_id]
    raise HTTPException(status_code=404, detail="Task not found")

# Create a new task
@app.post("/tasks", response_model=Task)
async def create_task(task_data: TaskCreate):
    task_id = len(tasks) + 1 # generate ID dinamically
    new_task = Task(id=task_id, title=task_data.title, description=task_data.description)
    tasks[task_id] = new_task
    return new_task

# PATCH endpoint to update a task's status
@app.patch("/tasks/{task_id}/status", response_model=Task)
async def update_task_status(task_id:int, update: TaskUpdate):
    if task_id in tasks:
        tasks[task_id].status = update.status
        return tasks[task_id]
    raise HTTPException(status_code=404, detail= "Task not found")
