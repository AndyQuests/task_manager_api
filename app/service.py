import asyncio
from app.models import Task

class TaskService:
    # TaskService doesn not create storage, it receives storage
    def __init__(self, storage: dict):
        self.storage = storage

    def get_task_or_404(self, task_id: int) -> Task:
        if task_id not in self.storage:
            raise Exception("Task not found")
        return self.storage[task_id]

    async def get_tasks(self):
        await asyncio.sleep(0.1)
        return self.storage.values()

    async def get_task_by_id(self, task_id):
        await asyncio.sleep(0.1) # Simulate DB latency
        task = self.get_task_or_404(task_id)
        return task

    async def create_task(self, task_data):
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