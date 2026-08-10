# User Stories - Task Tracker

## Core Features

### 1. Create a Task
- **As a** user,
- **I want to** add a new task with a title, description, and due date,
- **So that** I can keep track of things I need to accomplish.

### 2. View Tasks
- **As a** user,
- **I want to** retrieve a list of all tasks,
- **So that** I can review my current workload and priorities.

### 3. Update Task Status
- **As a** user,
- **I want to** mark a task as completed or pending,
- **So that** I can track my progress accurately.

### 4. Delete a Task
- **As a** user,
- **I want to** remove tasks that are no longer relevant,
- **So that** my task list remains clean and organized.

---

## Mid-Course Features

### Feature 1: Tag Filtering

1. **User Story:** As a user, I want to filter my tasks by specific tags so that I can view only the tasks relevant to a specific context.
   - **Acceptance Criteria:**
     - Sending `GET /tasks?tag=work` returns only tasks containing "work" in their `tags` list.

2. **User Story:** As a user, I want to apply multiple tags to a task so that I can organize tasks across multiple categories.
   - **Acceptance Criteria:**
     - Tasks accept an array/list of string tags during creation or update.

3. **User Story:** As a user, I want the system to return an empty list when filtering by a non-existent tag so that I know no matching tasks were found.
   - **Acceptance Criteria:**
     - Requesting `GET /tasks?tag=nonexistent` returns HTTP 200 with `[]`.

4. **User Story (Corrected AI Assumption):** As a user, I want tag filtering to perform exact substring/string matching regardless of letter case.
   - **Corrected AI Assumption:** The AI initially assumed tag filtering should be strict case-sensitive matching. I corrected this so that filtering converts tags to lowercase internally, ensuring `tag=Work` and `tag=work` return the same results.

---

### Feature 2: Overdue Status Tracking

1. **User Story:** As a user, I want to filter tasks that are past their due date so that I can focus on overdue items.
   - **Acceptance Criteria:**
     - Sending `GET /tasks?overdue=true` filters tasks where `due_date` is earlier than today and status is not `done`.

2. **User Story:** As a user, I want completed tasks with past due dates to be excluded from overdue filters so that only actionable items appear.
   - **Acceptance Criteria:**
     - Tasks marked as `done` are excluded from `GET /tasks?overdue=true` results even if their `due_date` is in the past.

3. **User Story:** As a user, I want clear error messaging if I pass an invalid boolean value to the overdue query parameter.
   - **Acceptance Criteria:**
     - Requesting `GET /tasks?overdue=invalid` returns HTTP 422 / HTTP 400 validation error response.

4. **User Story (Corrected AI Assumption):** As a user, I want overdue filtering to dynamically compare against the current UTC date at request time.
   - **Corrected AI Assumption:** The AI initially assumed comparing due dates against a fixed hardcoded date string in the test suite. I corrected this to use dynamic real-time UTC date checks (`datetime.now(timezone.utc)`), preventing false test failures when run on different dates.
  
## Implemented Features

### Feature 1: Overdue Filtering
* **As a** user,
* **I want to** filter my tasks to show only those that are past their due date,
* **So that** I can quickly identify and prioritize urgent overdue items.


  ## Overdue Task Filtering

### User Story
As a user, I want to filter my tasks to show only overdue tasks, so that I can quickly identify tasks that need immediate attention.

### Acceptance Criteria
- The user can filter the task list to show overdue tasks.
- A task is considered overdue when its due date has passed and it has not been completed.
- When the overdue filter is selected, only overdue tasks are displayed.
- The user can remove the filter and return to the full task list.

## Task Tags

### User Story
As a user, I want to add tags to my tasks, so that I can organize and categorize my tasks more easily.

### Acceptance Criteria
- The user can add a tag to a task.
- The task displays its assigned tag.
- The user can use tags to identify and organize tasks.
- Tasks without tags can still be created and managed normally.

### Feature 2: Tags / Labeling
* **As a** user,
* **I want to** add custom tags/labels to my tasks,
* **So that** I can categorize and organize tasks based on topics or context.
