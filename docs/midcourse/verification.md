
# Mid-Course Verification and Break Test Evidence

This document provides step-by-step evidence that the automated test suite effectively catches regressions and deliberate errors within the Task Tracker application.

## 1. Initial Test Suite Baseline

Prior to conducting deliberate defect tests, the test suite was executed to establish a passing baseline.

Command:
pytest

Output:
============================== test session starts ==============================
collected 5 items

tests/test_main.py .....                                                 [100%]

=============================== 5 passed in 0.12s ===============================


## 2. Break Test 1: Endpoint Response Verification

### Step 1: Deliberate Defect Introduction
In the root health-check endpoint, the HTTP response status code was deliberately modified from 200 to 500.

Original Code:
def read_root():
    return {"status": "ok"}

Modified Code (Defect Introduced):
def read_root(response: Response):
    response.status_code = 500
    return {"status": "ok"}

### Step 2: Test Failure Confirmation
Running pytest verified that the automated suite immediately detected the regression and flagged a failure.

Command:
pytest tests/test_main.py -k test_read_root

Output (Failure Caught):
_________________________________ test_read_root _________________________________

    def test_read_root():
        response = client.get("/")
>       assert response.status_code == 200
E       assert 500 == 200

tests/test_main.py:8: AssertionError
=========================== 1 failed in 0.15s ===========================

### Step 3: Code Restoration
The defect was reverted, restoring status code 200. Running pytest confirmed the test passed again.

Command:
pytest tests/test_main.py -k test_read_root

Output (Pass):
============================== test session starts ==============================
tests/test_main.py .                                                     [100%]

=============================== 1 passed in 0.08s ===============================


## 3. Break Test 2: Task Schema Validation

### Step 1: Deliberate Defect Introduction
In the task creation logic, the returned payload dictionary key for task title was altered from title to task_title.

Original Code:
def create_task(task: TaskSchema):
    return {"id": 1, "title": task.title, "completed": False}

Modified Code (Defect Introduced):
def create_task(task: TaskSchema):
    return {"id": 1, "task_title": task.title, "completed": False}

### Step 2: Test Failure Confirmation
Running pytest confirmed that the test failed as expected.

Command:
pytest tests/test_main.py -k test_create_task

Output (Failure Caught):
________________________________ test_create_task ________________________________

    def test_create_task():
        response = client.post("/tasks/", json={"title": "New Task"})
        assert response.status_code == 200
>       assert "title" in response.json()
E       AssertionError: assert 'title' in {'id': 1, 'task_title': 'New Task', 'completed': False}

tests/test_main.py:18: AssertionError
=========================== 1 failed in 0.14s ===========================

### Step 3: Code Restoration
The key was restored back to title.

Command:
pytest

Output (Pass):
============================== test session starts ==============================
collected 5 items

tests/test_main.py .....                                                 [100%]

=============================== 5 passed in 0.12s ===============================
