from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ===============
#   TEST CREATE
# ===============

def test_create_task_rejects_missing_title():
    response = client.post("/tasks", json={
        "description": "no-title",
    })
    assert response.status_code == 422 # 422 = Unprocessable Entity

def test_create_task_rejects_empty_title():
    response = client.post("/tasks", json={
        "title": "",
        "description": "empty-title"
    })
    assert response.status_code == 422

def test_create_task_rejects_too_long_title():
    long_title = "x" * 101
    response = client.post("/tasks", json={
        "title": f"{long_title}",
        "description": "too-long-title"
    })    
    assert response.status_code == 422

def test_create_task_accepts_no_description():
    response = client.post("/tasks", json={
        "title": "no-description-provided"
    })
    assert response.status_code == 200

def test_create_task_rejects_empty_description():
    response = client.post("/tasks", json={
        "title": "empty-description-provided",
        "description": ""
    })
    assert response.status_code == 422

def test_create_task_rejects_too_long_description():
    long_description = "x" * 301
    response = client.post("/tasks", json={
        "title": "Too-long-description",
        "description": f"{long_description}"
    })
    assert response.status_code == 422

def test_create_task_default_status_is_pending():
    response = client.post("/tasks", json={
        "title": "Test-default-status",
        "description": "status-not-specified"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "pending"

# ===============
#   TEST UPDATE
# ===============

def test_update_task_rejects_empty_title():
    client.post("/tasks", json={
        "title": "empty-title-update",
    })

    response = client.patch("/tasks/1", json={
        "title": ""
        })
    assert response.status_code == 422

def test_update_task_rejects_too_long_title():
    long_title = "x" * 101
    client.post("/tasks", json={
        "title": "too-long-title-update"
    })

    response = client.patch("/tasks/1", json={
        "title": f"{long_title}"
        })    
    assert response.status_code == 422

def test_update_task_rejects_empty_description():
    client.post("/tasks", json={
        "title": "unchanged-title",
        "description": "empty-description-update"
    })

    response = client.patch("/tasks/1", json={
        "description": ""
    })
    assert response.status_code == 422

def test_update_task_rejects_too_long_description():
    long_description = "x" * 301
    client.post("/tasks", json={
        "title": "unchanged-title",
        "description": "long-description-update"
    })

    response = client.patch("/tasks/1", json={
        "description": f"{long_description}"
    })
    assert response.status_code == 422

def test_update_task_rejects_invalid_status():
    client.post("/tasks", json={
        "title": "unchanged-title",
        "description": "unchanged-description"
    })

    response = client.patch("/tasks/1", json={
        "status": "paused"
        })
    assert response.status_code == 422

def test_update_task_accepts_no_fields():
    client.post("/tasks", json={
        "title": "unchanged-title",
        "description": "unchanged-description"
    })

    response = client.patch("/tasks/1", json={})
    assert response.status_code == 200
    assert response.json()["title"] == "unchanged-title"
    assert response.json()["description"] == "unchanged-description"