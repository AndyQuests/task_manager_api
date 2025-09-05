from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)

# Reset list before each test
def setup_function():
    tasks.clear()

def test_create_task_missing_title():
    response = client.post("/tasks", json={
        "description": "No title",
    })
    assert response.status_code == 422 # 422 = Unprocessable Entity