# 🧪 Test Directory

This folder contains unit tests for the Task Manager FastAPI project.

## Structure
- `test_main.py`
Test related to task functionality / CRUD functionality:
    - Creating a task
    - Retreiving all tasks
    - Retrieving a single task by ID
    - Getting a task that doesn't exist (future test_errors.py)
* This is expected to be removed as the project grows and these tests are splitted

# Test getting a task that doesn't exist
- `test_validation.py`
Test for input validation and schema constraints:
    - Missing required fields
    - Invalid data types
    - Default values 

- `test_status.py`
Test for status logic
    - Default Status is Pending
    - Update Status
    - Update with invalid status
    - Update status with invalid id

## Running Tests

From the project root:
```bash
pytest -s