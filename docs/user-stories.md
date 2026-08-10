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
 
## Feature 5: Overdue Filtering

**User Story:**
As a user, I want to filter my task list to display only overdue tasks, so that I can quickly identify and address missed deadlines.

**Acceptance Criteria:**
- The system provides a filter option for "Overdue" tasks.
- When selected, only tasks with a due date in the past and a status other than "Completed" are displayed.
- If no tasks are overdue, an empty state message is shown.

---

## Feature 6: Tags Management

**User Story:**
As a user, I want to add, view, and filter tasks by custom tags, so that I can categorize and organize my workload effectively.

**Acceptance Criteria:**
- Users can attach one or more tags (e.g., `work`, `urgent`) when creating or updating a task.
- Tags are visually displayed alongside each task in the list.
- Users can click or filter by a specific tag to view only related tasks.


  ## Feature: Overdue Filtering

### User Story
**As a** busy user managing multiple deadlines,  
**I want to** filter my tasks to show only those that are overdue,  
**So that** I can quickly identify and focus on urgent tasks that missed their due date.

### Acceptance Criteria
- A filter option or button for "Overdue" is visible on the main task view.
- When activated, the list filters to display only tasks whose due date is in the past and are not marked as completed.
- If there are no overdue tasks, a clear indicator/message (e.g., "No overdue tasks") is displayed.

---

## Feature: Task Tags & Categorization

### User Story
**As a** user organizing diverse projects,  
**I want to** assign custom tags to my tasks and filter tasks by specific tags,  
**So that** I can group, categorize, and locate related items efficiently across different categories.

### Acceptance Criteria
- Users can create and attach one or more tags to a task during task creation or editing.
- Applied tags are visibly displayed on each task item/card in the list.
- Users can click a tag or select a tag filter to view only tasks associated with that specific tag.
- Users can edit or remove tags from an existing task.

### Feature 2: Overdue Status Tracking
- **User Story:** As a user, I want to filter tasks that are past their due date so that I can focus on overdue items.
- **Acceptance Criteria:**
  - Sending `GET /tasks?overdue=true` filters tasks where `due_date` is earlier than today and status is not `done`.
