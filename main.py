from fastapi import FastAPI
from fastapi import HTTPException # Let us return proper status codes (e.g. 404)
from pydantic import BaseModel  # Pydantic handles input validation
from typing import Optional, List

app = FastAPI()

# In-memory task storage
tasks = []

# Task Data Model
class Task(BaseModel): 
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

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
