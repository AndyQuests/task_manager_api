# 🧪 Test Directory

This folder contains unit tests for the Task Manager FastAPI project.
Tests are structured to ensure a clear separation between service-layer unit tests and API-layer tests.

## Structure

- `conftest.py`
Special _config_ file, defines shared test behaviour
    - Fixture `clear_tasks` resets task storage before each test
    - Fixture `client` initializes the Fast API test client
    - Fixture `no_sleep` mocks asynchronous wait for faster async tests

    Note: conftest.py is automatically discovered by pytest and makes these fixtures available to all test modules without explicit imports.

- `test_service.py`
Unit tests for the service layer(business logic only):
    - Task creation
    - Task retrieval
    - Task updates
    - Task deletion

- `test_tasks.py`
Test for API endpoints:
    - Routing
    - Response status codes
    - Response models
    - Service integration

- `test_validation.py`
Test for input validation and schema constraints in API layer:
    - Missing fields
    - Invalid values
    - Model rules (parameter constraints, default values)


## Running Tests

From the project root:
```bash
pytest -s