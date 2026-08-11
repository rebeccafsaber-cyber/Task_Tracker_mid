# User Stories & Acceptance Criteria - Task Tracker

This document provides a consolidated list of user stories and explicit acceptance criteria for the Task Tracker application, covering both core functions and mid-course feature additions.

---

## Core Task Management

### 1. Create a Task
* **As a** user,
* **I want to** create a new task with a title and description,
* **So that** I can track my personal assignments.

**Acceptance Criteria:**
* Sending a `POST` request to `/tasks/` creates a task record.
* Title field is mandatory; missing titles trigger an HTTP `422 Unprocessable Entity` error.
* Successful creation returns HTTP `201 Created` with the generated task object.

---

### 2. View Tasks
* **As a** user,
* **I want to** retrieve all tasks,
* **So that** I can review my current workload.

**Acceptance Criteria:**
* Sending a `GET` request to `/tasks/` returns a JSON array of all existing tasks.
* Returns HTTP `200 OK`. Returns an empty list `[]` if no tasks are present.

---

### 3. Update Task Status & Details
* **As a** user,
* **I want to** update a task's title, description, or completion status,
* **So that** I can keep my task list up to date.

**Acceptance Criteria:**
* Sending a `PUT` request to `/tasks/{task_id}` updates the matching task.
* Returns HTTP `200 OK` with the updated task object.
* Invalid `task_id` returns HTTP `404 Not Found` with a detail message.

---

### 4. Delete a Task
* **As a** user,
* **I want to** delete an existing task,
* **So that** I can remove tasks that are no longer relevant.

**Acceptance Criteria:**
* Sending a `DELETE` request to `/tasks/{task_id}` removes the task.
* Returns HTTP `200 OK` upon successful removal.
* Non-existent `task_id` returns HTTP `404 Not Found`.

---

## Mid-Course Enhanced Features

### 5. Tag Management & Filtering
* **As a** user,
* **I want to** attach custom string tags to tasks and filter tasks by specific tags,
* **So that** I can organize tasks across different contexts.

**Acceptance Criteria:**
* Tasks accept an array of strings in the `tags` field during creation or update.
* Sending `GET /tasks?tag=work` returns only tasks containing `"work"` in their tags array.
* Tag filtering is case-insensitive (e.g., `tag=Work` matches `work`).
* Querying a non-existent tag returns HTTP `200 OK` with an empty array `[]`.

---

### 6. Overdue Task Tracking
* **As a** user,
* **I want to** filter tasks that are past their due date,
* **So that** I can identify urgent overdue items.

**Acceptance Criteria:**
* Sending `GET /tasks?overdue=true` filters tasks where `due_date` is earlier than the current UTC time and status is incomplete (`completed=false`).
* Tasks marked as completed (`completed=true`) are excluded from overdue filtering even if their due date is in the past.
* Passing an invalid non-boolean value to the `overdue` parameter returns an HTTP `422` validation error.
