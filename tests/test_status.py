from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)

def setup_function():
    tasks.clear()

def test_update_task_status():
    client.post("/tasks", json={
        "id": 5,
        "title": "Status Test",
        "description": "Testing status update",
        "completed": False
    })

    response = client.patch("/tasks/5/status?status=in_progress")
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"

def test_update_status_invalid_id():
    response = client.patch("/tasks/999/status?status=completed")
    assert response.status_code == 404

def test_update_status_invalid_value():
    client.post("/tasks", json={
        "id": 5,
        "title": "Invalid status test",
        "description": "Try invalid status"
    })

    response = client.patch("/tasks/5/status?status=paused")
    assert response.status_code == 422


