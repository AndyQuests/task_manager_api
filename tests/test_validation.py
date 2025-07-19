from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)

# Reset list before each test
def setup_function():
    tasks.clear()

def test_create_task_missing_title():
    response = client.post("/tasks", json={
        "id": 3,
        "description": "No title",
        "completed": False
    })
    assert response.status_code == 422 # 422 = Unprocessable Entity

def test_create_task_invalid_id_type():
    response = client.post("/tasks", json={
        "id": "not-an-integer",
        "title": "Invalid ID type",
        "description": "Should return 422",
        "completed": False
    })
    assert response.status_code == 422

def test_create_task_without_completed_field():
    response = client.post("/tasks", json={
        "id": 0,
        "title": "Default 'completed' test",
        "description": "'completed' should default to False"
    })
    assert response.status_code == 200
    assert response.json()["completed"] == False # Should default to False