import asyncio
from app.models import Task, TaskCreate, TaskUpdate
from typing import List

class TaskNotFoundError(Exception):
    pass

class TaskService:
    # TaskService doesn not create storage, it receives storage
    def __init__(self, storage: dict):
        self.storage = storage

    def get_task_or_404(self, task_id: int) -> Task:
        if task_id not in self.storage:
            raise TaskNotFoundError("Task not found")
        return self.storage[task_id]

    async def get_tasks(self) -> List[Task]:
        await asyncio.sleep(0.1)
        return list(self.storage.values())

    async def get_task_by_id(self, task_id: int) -> Task:
        await asyncio.sleep(0.1) # Simulate DB latency
        task = self.get_task_or_404(task_id)
        return task

    async def create_task(self, task_data: TaskCreate) -> Task:
        await asyncio.sleep(0.3) # simulate DB write delay
        # generate ID dinamically
        task_id = len(self.storage) + 1

        new_task = Task(
            id = task_id,
            title = task_data.title,
            description = task_data.description
        )

        self.storage[task_id] = new_task
        return new_task
    
    async def update_task(self, task_id: int, update_data: TaskUpdate) -> Task:
        await asyncio.sleep(0.2)
        stored_task = self.get_task_or_404(task_id)
        
        update_dict = update_data.model_dump(exclude_unset=True)
        
        for field, value in update_dict.items():
            setattr(stored_task, field, value)
        
        return stored_task
    
    async def delete_task(self, task_id: int) -> None:
        await asyncio.sleep(0.2)
        self.get_task_or_404(task_id)
        del self.storage[task_id]