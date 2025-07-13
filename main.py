from fastapi import FastAPI
from pydantic import BaseModel  # Pydantic. Validates incoming data
from typing import Optional, List

app = FastAPI()

# Temporary in-memory task store
tasks = []

# Task data model
class Task(BaseModel):  # Uses pydantic
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/tasks")
async def create_task(task: Task):
    tasks.append(task)
    return tasks