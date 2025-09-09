from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)

def setup_function():
    tasks.clear()

def test_task_default_status_is_pending():
    response = client.post("/tasks", json={
        "title": "Task without status",
        "description": "Testing default status"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "pending"

def test_update_task_status():
    client.post("/tasks", json={
        "title": "Status Test",
        "description": "Testing status update",
    })

    response = client.patch("/tasks/1/status", json={"status": "in_progress"})
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"

def test_update_status_invalid_id():
    response = client.patch("/tasks/999/status", json={"status": "completed"})
    assert response.status_code == 404

def test_update_status_invalid_value():
    client.post("/tasks", json={
        "title": "Invalid status test",
        "description": "Try invalid status"
    })

    response = client.patch("/tasks/1/status", json={"status": "paused"})
    assert response.status_code == 422


