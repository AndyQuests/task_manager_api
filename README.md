# A FastAPI-based task manager with CRUD operations and validation tests.

## **Quickstart**

  ```bash
  git clone <repo-url>
  cd task_manager
  pip install -r requirements.txt
  uvicorn app.main:app --reload
  ```

## **Available endpoints**
  HTTP method + path + description

  ```
  POST   /tasks        → Create a new task
  GET    /tasks        → List all tasks
  GET    /tasks/{id}   → Get a single task
  PATCH  /tasks/{id}   → Update title, description, or status
  DELETE /tasks/{id}   → Delete a task
  ```

## **Validation rules**

  * Title: 1–100 chars, required
  * Description: optional, max 300 chars
  * Status: one of `"pending" | "in-progress" | "completed"`

## **Running tests**

  ```bash
  pytest -s
  ```

## **Project overview**

  ```
  app/
    main.py        → FastAPI app & routes
    models.py      → Pydantic models
  tests/
    test_validation.py  → Data validation
    test_tasks.py       → Test CRUD
  ```

* **Design choices**

  * Unified PATCH endpoint for updates.
  * Validation handled by Pydantic (string coercion, min/max lengths).
  * Tests split by responsibility:

    * `test_validation.py`: input validation
    * `test_tasks.py`: core CRUD

    For more details on the testing strategy, 
    see [app/tests/README.md](app/tests/README.md).

* **Next steps**
    * Add database support instead of in-memory storage" 
    * "Implement filtering by status."