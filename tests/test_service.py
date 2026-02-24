import pytest

from app.models import TaskCreate, TaskUpdate
from app.service import TaskNotFoundError, TaskService

@pytest.fixture
def service():
    """Create a fresh service instance for each test"""
    storage = {}
    return TaskService(storage)

@pytest.mark.asyncio
async def test_create_task_assigns_incrementing_ids(service):
    first_task = await service.create_task(
        TaskCreate(
            title="First task",
            description="Check increasing ids"
        )
    )
    second_task = await service.create_task(
        TaskCreate(
            title="Second task",
            description="Check increasing ids"
        )
    )
    assert first_task.id == 1
    assert second_task.id == 2

@pytest.mark.asyncio
async def test_get_tasks_return_all_existing(service):
    assert await service.get_tasks() == []
    
    first_task = await service.create_task(
        TaskCreate(
            title="First task",
            description="Check if returned"
        )
    )
    second_task = await service.create_task(
        TaskCreate(
            title="Second task",
            description="Check if returned"
        )
    )

    tasks = await service.get_tasks()
    assert len(tasks) == 2
    assert first_task in tasks
    assert second_task in tasks

@pytest.mark.asyncio
async def test_get_task_by_id_returns_correct_task(service):
    created_task = await service.create_task(
        TaskCreate(
            title="New title",
            description="Check if retrieved",
            status="pending"
        )
    )

    retrieved = await service.get_task_by_id(created_task.id)
    assert retrieved.id == created_task.id
    assert retrieved.title == "New title"
    assert retrieved.description == "Check if retrieved"
    assert retrieved.status == "pending"

@pytest.mark.asyncio
async def test_get_task_by_id_raises_when_missing(service):
    with pytest.raises(TaskNotFoundError):
        await service.get_task_by_id(1)

@pytest.mark.asyncio
async def test_update_task_single_field(service):
    created_task = await service.create_task(
        TaskCreate(
            title="Original title",
            description="Original description"
        )
    )

    updated_task = await service.update_task(
        created_task.id,
        TaskUpdate(title="Updated title")
    )
    
    assert updated_task.title == "Updated title"
    assert updated_task.description == "Original description"
    assert updated_task.status == "pending"

@pytest.mark.asyncio
async def test_update_task_multiple_fields(service):
    created_task = await service.create_task(
        TaskCreate(
            title="Original title",
            description="Original description"
        )
    )

    updated_task = await service.update_task(
        created_task.id,
        TaskUpdate(
            title="Updated title",
            description="Updated description",
            status="in_progress"
        )
    )

    assert updated_task.title == "Updated title"
    assert updated_task.description == "Updated description"
    assert updated_task.status == "in_progress"

@pytest.mark.asyncio
async def test_update_task_can_clear_description(service):
    created_task = await service.create_task(
        TaskCreate(
            title="Original title",
            description="This will be cleared"
        )
    )
    
    updated_task = await service.update_task(
        created_task.id,
        TaskUpdate(description=None)
    )

    assert updated_task.description is None

@pytest.mark.asyncio
async def test_update_task_raises_when_missing(service):
    with pytest.raises(TaskNotFoundError):
        await service.update_task(1, TaskUpdate(title="Any title"))

@pytest.mark.asyncio
async def delete_removes_task():
    created_task = await service.create_task(
        TaskCreate(
            title="Original title",
            description="This task will be removed"
        )
    )
    removed_task_id = created_task.id
    await service.delete_task(created_task.id)
    
    with pytest.raises(TaskNotFoundError):
        await service.get_task_by_id(removed_task_id)

@pytest.mark.asyncio
async def delete_raises_when_missing(service):
    with pytest.raises(TaskNotFoundError):
        await service.delete_task(1)