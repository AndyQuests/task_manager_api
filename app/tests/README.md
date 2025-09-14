# 🧪 Test Directory

This folder contains unit tests for the Task Manager FastAPI project.

## Structure

- `confest.py`
Special _config_ file, defines shared test behaviour
    - Fixture `no_sleep` to mock asyncronous wait for faster async tests

- `test_main.py`
Test related to task functionality / CRUD functionality:
    - Task creation
    - Task retrieval
    - Getting a task that doesn't exist (future test_errors.py)
    - Task updates
    - Task deletion
* This is expected to be removed as the project grows and these tests are splitted

- `test_validation.py`
Test for input validation and schema constraints:
    - Missing fields
    - Invalid values
    - Model rules (parameter constraints, default values)

## Running Tests

From the project root:
```bash
pytest -s