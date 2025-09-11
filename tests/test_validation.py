from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)

# Reset list before each test
def setup_function():
    tasks.clear()

def test_create_task_missing_title():
    response = client.post("/tasks", json={
        "description": "no-title",
    })
    assert response.status_code == 422 # 422 = Unprocessable Entity

def test_create_task_invalid_title_type():
    response = client.post("/tasks", json={
        "title" : 0,
        "description": "integer-title",
    })
    assert response.status_code == 422

def test_create_task_empty_title():
    response = client.post("/tasks", json={
        "title": "",
        "description": "empty-title"
    })
    assert response.status_code == 422

def test_create_task_too_long_title():
    long_title = "x" * 101
    response = client.post("/tasks", json={
        "title": f"{long_title}",
        "description": "too-long-title"
    })    
    assert response.status_code == 422

def test_create_task_no_description():
    response = client.post("/tasks", json={
        "title": "no-description-provided"
    })
    assert response.status_code == 200

def test_create_task_empty_description():
    response = client.post("/tasks", json={
        "title": "empty-description-provided",
        "description": ""
    })
    assert response.status_code == 422

def test_create_task_invalid_description_type():
    response = client.post("/tasks", json={
        "title" : "Integer-description",
        "description": 0,
    })
    assert response.status_code == 422

def test_create_task_too_long_description():
    long_description = "x" * 301
    response = client.post("/tasks", json={
        "title": "Too-long-description",
        "description": f"{long_description}"
    })
    assert response.status_code == 422