# User Stories - Task Tracker

## 1. Create a Task
* **As a** user,
* **I want to** add a new task with a title, description, and due date,
* **So that** I can keep track of things I need to accomplish.

## 2. View Tasks
* **As a** user,
* **I want to** retrieve a list of all tasks,
* **So that** I can review my current workload and priorities.

## 3. Update Task Status
* **As a** user,
* **I want to** mark a task as completed or pending,
* **So that** I can track my progress accurately.

## 4. Delete a Task
* **As a** user,
* **I want to** remove tasks that are no longer relevant,
* **So that** my task list remains clean and organized.

## Mid-Course Features

### Feature 1: Tag Filtering
- **User Story:** As a user, I want to filter my tasks by specific tags so that I can view only the tasks relevant to a specific context.
- **Acceptance Criteria:**
  - Sending `GET /tasks?tag=work` returns only tasks containing "work" in their `tags` list.

### Feature 2: Overdue Status Tracking
- **User Story:** As a user, I want to filter tasks that are past their due date so that I can focus on overdue items.
- **Acceptance Criteria:**
  - Sending `GET /tasks?overdue=true` filters tasks where `due_date` is earlier than today and status is not `done`.
