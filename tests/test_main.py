from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)

# Reset the list before each test
def setup_function():
    tasks.clear()

# Test creating a task (POST /tasks) 
def test_create_task():
    # Create a task to retrieve
    response = client.post("/tasks", json ={
        "title" : "Test task",
        "description" : "Added for retrieval",
    })

    assert response.status_code == 200
    assert response.json()["title"] == "Test task"

# Test retreiving all tasks (GET /tasks) 
def test_get_tasks():
    # Create a task to retrieve
    response = client.post("/tasks", json ={
        "title" : "Test task",
        "description" : "Added for retrieval",
    })

    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(task["title"] == "Test task" for task in response.json())

# Test retrieving a single task by ID (GET /tasks/{id})
def test_get_task_by_id():
    # Create a task to retrieve
    create_response = client.post("/tasks", json={
        "title": "Task by ID",
        "description": "Testing GET by ID",
    })
    task_id = create_response.json()["id"]
    # Fetch the task by that id
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Task by ID"

# Test getting a task that doesn't exist
def test_get_task_invalid_id():
    response = client.get("tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"