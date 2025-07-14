from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test creating a single task (POST /tasks) 
def test_create_task():
    # Create a task to retrieve
    response = client.post("/tasks", json ={
        "id" : 1,
        "title" : "Test task",
        "description" : "Unit test",
        "completed" : False
    })
    print(response.json())  # 👈 Debug print
    assert response.status_code == 200
    assert response.json()["title"] == "Test task"

# Test retreiving all tasks (GET /tasks) 
def test_get_tasks():
    response = client.get("/tasks")
    print(response.json())  # 👈 Debug print
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(task["title"] == "Test task" for task in response.json())

# Test retrieving a single task by ID (GET /tasks/{id})
def test_get_task_by_id():
    # Create a task to retrieve
    client.post("/tasks", json={
        "id": 2,
        "title": "Task by ID",
        "description": "Testing GET by ID",
        "completed": False
    })

    response = client.get("/tasks/2")
    assert response.status_code == 200
    assert response.json()["title"] == "Task by ID"

# Test getting a task that doesn't exist
def test_get_task_invalid_id():
    response = client.get("tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"