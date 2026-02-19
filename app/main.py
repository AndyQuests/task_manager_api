from app.models import Task, TaskCreate, TaskUpdate
from app.service import TaskService, TaskNotFoundError
from app.storage import tasks
from fastapi import FastAPI, Depends
from fastapi import HTTPException # Let us return proper status codes
from typing import List 

# ---------------------
#       1. APP 
# ---------------------

app = FastAPI()

# ---------------------
#       3. HELPER FUNCTIONS
# ---------------------

# Dependency Provider
def get_task_service():
    return TaskService(tasks)

# ---------------------
#       3. ENDPOINTS
# ---------------------

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks(
    service: TaskService = Depends(get_task_service)):
    return await service.get_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(
    task_id: int,
    service: TaskService = Depends(get_task_service)):
    try:
        return await service.get_task_by_id(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/tasks", response_model=Task)
async def create_task(
    task_data: TaskCreate,
    service: TaskService = Depends(get_task_service)):
    return await service.create_task(task_data)

@app.patch(
        "/tasks/{task_id}",
        description="Partially updates a task. Only provided fields are modified",
        response_model=Task
        )
async def update_task(
    task_id: int,
    update_data: TaskUpdate,
    service: TaskService = Depends(get_task_service)):
    try:
        return await service.update_task(task_id, update_data)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)):
    try:
        await service.delete_task(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))