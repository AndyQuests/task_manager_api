def test_create_task(client):
    response = client.post("/tasks", json ={
        "title" : "Test task",
        "description" : "Added for retrieval",
    })

    assert response.status_code == 200
    assert response.json()["title"] == "Test task"

# ===============
#   TEST GET
# ===============

def test_get_tasks(client):
    # Create a task to retrieve
    response = client.post("/tasks", json ={
        "title" : "Test task",
        "description" : "Added for retrieval",
    })
    # Fetch all existing tasks
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(task["title"] == "Test task" for task in response.json())

def test_get_task_by_id_success(client):
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

def test_get_task_invalid_id(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

# ===============
#   TEST UPDATE
# ===============

def test_update_task_title_only(client):
    client.post("/tasks", json={
        "title": "only-update-title",
        "description": "unchanged-description"
    })
    response = client.patch("/tasks/1", json={
        "title": "updated-title"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "updated-title"
    assert response.json()["description"] == "unchanged-description"

def test_update_task_description_only(client):
    client.post("/tasks", json={
        "title": "unchanged-title",
        "description": "only-update-this-description"
    })

    response = client.patch("/tasks/1", json={
        "description": "updated-description"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "unchanged-title"
    assert response.json()["description"] == "updated-description"

def test_update_task_status_only(client):
    client.post("/tasks", json={
        "title": "unchanged-title",
        "description": "unchanged-description",
    })

    response = client.patch("/tasks/1", json={"status": "in_progress"})
    assert response.status_code == 200
    assert response.json()["title"] == "unchanged-title"
    assert response.json()["description"] == "unchanged-description"
    assert response.json()["status"] == "in_progress"

def test_update_task_multiple_fields(client):
    client.post("/tasks", json={
        "title": "updating-multiple-fields",
        "description": "running-updates",
        "status": "pending"
    })
    response = client.patch("/tasks/1", json={
        "title": "updated-title",
        "description": "updated-description",
        "status": "completed"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "updated-title"
    assert response.json()["description"] == "updated-description"
    assert response.json()["status"] == "completed"

def test_update_non_existing_task(client):
    response = client.patch("/tasks/999", json={
        "title": "updated-title",
        "description": "updated-description",
        "status": "completed"
    })
    assert response.status_code == 404

# ===============
#   TEST DELETE
# ===============

def test_delete_task_success(client):
    client.post("/tasks", json={
        "title": "test-delete-task",
        "description": "test-delete-tasks"
    })
    assert client.get("/tasks/1").status_code == 200
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert client.get("/tasks/1").status_code == 404

def test_delete_task_non_existent(client):
    response = client.delete("/tasks/1")
    assert response.status_code == 404

def test_delete_task_twice(client):
    client.post("/tasks", json={
        "title": "test-delete-twice",
        "description": "test-delete-twice"
    })

    assert client.get("/tasks/1").status_code == 200
    assert client.delete("/tasks/1").status_code == 200
    assert client.delete("/tasks/1").status_code == 404