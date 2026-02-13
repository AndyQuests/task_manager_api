# 🧪 Test Directory

This folder contains unit tests for the Task Manager FastAPI project.

## Structure

- `conftest.py`
Special _config_ file, defines shared test behaviour
    - Fixture `clear_tasks` resets task storage before each test
    - Fixture `client` initializes the Fast API test client
    - Fixture `no_sleep` mocks asynchronous wait for faster async tests

    * Note. conftest.py is automatically discovered by pytest and makes these fixtures available to all test modules without explicit imports.

- `test_tasks.py`
Test related to task functionality / CRUD functionality:
    - Task creation
    - Task retrieval
    - Task retrieve invalid task (future test_errors.py)
    - Task updates
    - Task deletion

- `test_validation.py`
Test for input validation and schema constraints:
    - Missing fields
    - Invalid values
    - Model rules (parameter constraints, default values)


## Running Tests

From the project root:
```bash
pytest -s