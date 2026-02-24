# Task Manager API 
A RESTful API for managing tasks built with FastAPI.

## Features
- CRUD operations: Create, read, update and delete tasks
- Data validation with Pydantic
- Asynchronous endpoints
- Dependency Injection
- Comprehensive testing: Unit tests with pytest and load testing with Locust
- Automatic API Documentation: Interactive Swagger UI

## Tech Stack
- Python 3.9
- FastAPI - Modern web framework
- Pydantic - Data validation
- pytest - Unit testing
- Locust - Load testing
- Uvicorn - ASGI server

## Prerequisites
- Python 3.9+
- pip (Python package manager)

## Getting Started
  ```bash
  git clone https://github.com/andyquests/task_manager_api
  cd task_manager
  ```

Create and activate a virtual environment:
  ```bash
  # On Windows
  python -m venv task_manager_venv
  venv\Scripts\activate

  # On macOS/Linux
  python -m venv task_manager_venv
  source task_manager_env/bin/activate
  ```

Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Running the API
Run the server:
  ```bash
  uvicorn app.main:app --reload
  ```

API will be available at: http://localhost:8000

## API Documentation
Once the server is running, you can access:

- Swagger UI: http://localhost:8000/docs

## Available endpoints
HTTP method |  Path |  Description
  ```
  POST   /tasks          Create a new task
  GET    /tasks          List all tasks
  GET    /tasks/{id}     Get a single task
  PATCH  /tasks/{id}     Update title, description, or status
  DELETE /tasks/{id}     Delete a task
  ```

## Validation rules
* Title: 1–100 chars, required
* Description: optional, must be null or not empty string, max 300 chars
* Status: one of `"pending" | "in-progress" | "completed"`

## Unit tests
  ```bash
  pytest -s
  ```
For more details on the testing strategy, 
see [app/tests/README.md](app/tests/README.md).

## Load Testing
With the server running, run Locust load tests:
  ```bash
  locust -f locustfile.py
  ```
Then open http://localhost:8089 to configure and start the test.

## Project overview
```
app/
  main.py        # FastAPI app & routes
  models.py      # Pydantic models
  service.py     # Business logic
  storage.py     # in-memory DB
tests/
  conftest.py    # Shared test fixtures
  test_service.py     # Bussiness logic unit tests
  test_tasks.py       # API endpoints
  test_validation.py  # API validation
```

* **Next steps**
  * Implement search or "filtering by status"
  * Add database support instead of in-memory storage"