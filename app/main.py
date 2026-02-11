from fastapi import FastAPI
from fastapi import HTTPException # Let us return proper status codes (e.g. 404)
from typing import List # Let us use List parameter types
import asyncio
from app.models import Task, TaskCreate, TaskUpdate
from app.storage import tasks

# ---------------------
#       1. APP 
# ---------------------

app = FastAPI()

# ---------------------
#       3. HELPER FUNCTIONS
# ---------------------

def get_task_or_404(task_id: int) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

# ---------------------
#       3. ENDPOINTS
# ---------------------

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@ app.get("/tasks", response_model=List[Task])
async def get_tasks():
    await asyncio.sleep(0.1)
    return tasks.values() ### < check

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int): 
    await asyncio.sleep(0.1) # simulate DB latency
    task = get_task_or_404(task_id)
    return task

@app.post("/tasks", response_model=Task)
async def create_task(task_data: TaskCreate):
    await asyncio.sleep(0.3) # simulate DB write delay
    task_id = len(tasks) + 1 # generate ID dinamically
    new_task = Task(id=task_id, 
                    title=task_data.title, 
                    description=task_data.description)
    tasks[task_id] = new_task
    return new_task

@app.patch(
        "/tasks/{task_id}",
        summary="Update Task",
        description="Partially updates a task. Only provided fields are modified",
        response_model=Task
        )
async def update_task(task_id:int, update: TaskUpdate):
    await asyncio.sleep(0.2)
    stored_task = get_task_or_404(task_id)

    if update.title:
        stored_task.title = update.title
    if update.description:
        stored_task.description = update.description
    if update.status:
        stored_task.status = update.status

    return stored_task

@app.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    await asyncio.sleep(0.2)
    get_task_or_404(task_id)
    del tasks[task_id]
    return {"message": "Task deleted successfully"}
