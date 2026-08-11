

# Mid-Course AI Prompt Log

This document records the prompt engineering workflow and specific LLM interactions used during the development of the Task Tracker mid-course features.

---

## 1. Feature Prompt History

| Feature / Task | Goal | Prompt Provided to AI | Outcome / Result |
| :--- | :--- | :--- | :--- |
| **Task Management** | Implement Pydantic model validation for Task CRUD | "Create a Pydantic schema for FastAPI that validates a task payload with a required `title` string (min length 1) and an optional `description` string." | Generated accurate Pydantic models with `BaseModel` and proper field validation. |
| **Task Routes** | Build POST and GET endpoints for `/tasks/` | "Write FastAPI endpoint handlers for `POST /tasks/` to create a task and `GET /tasks/` to fetch all tasks using an in-memory dictionary list." | Provided functional router handlers with correct HTTP status codes (`201` for post, `200` for get). |
| **Testing** | Write automated test cases using Pytest | "Write Pytest unit test functions using FastAPI `TestClient` to verify that `POST /tasks/` returns 201 and creates a task correctly." | Generated test cases covering endpoint status codes and JSON response structure verification. |

---

## 2. Weak vs. Strong Prompt Comparison

To demonstrate prompt engineering progression, below is a comparison showing how refining prompt specificity improved AI outputs during mid-course feature implementation.

### Example Scenario: Building Task Status Update Endpoint

#### ❌ Weak Prompt
> *"Make a route to update task status in FastAPI."*

* **Issues with Weak Output:** 
  * Produced generic, incomplete code without error handling.
  * Used incorrect HTTP methods and lacked type validation.
  * Omitted response models and proper HTTP status handling for non-existent task IDs (404 errors).

#### ✅ Strong Prompt
> *"Write a FastAPI router endpoint for `PUT /tasks/{task_id}` that accepts a JSON payload to update `title` or `completed` status. Include proper Pydantic schemas, return `200 OK` with the updated task model upon success, and raise an `HTTPException(status_code=404, detail='Task not found')` if the task ID does not exist in memory."*

* **Benefits of Strong Output:**
  * Generated production-ready FastAPI code with correct status code handling (`200 OK` and `404 Not Found`).
  * Enforced robust type safety using Pydantic.
  * Saved debugging time by correctly modeling edge cases upfront.
