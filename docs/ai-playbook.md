
# AI Playbook

## Rules & Decision Cards

### Rule 1: Schema Consistency
Always ensure that Pydantic response models (`TaskSchema`) mirror all required task fields: `id`, `title`, `description`, `status`, `tags`, `due_date`, and `completed`.

### Rule 2: Test Alignment
Every endpoint defined in `backend/main.py` must have an associated test case in the test suite ensuring expected HTTP status codes (e.g., 200 OK, 201 Created, 204 No Content).

### Decision Card: Overdue Filtering Logic
- **Condition**: Task has a defined `due_date`, the date is prior to the current date, and `completed` is `False`.
- **Action**: Include task in results when `overdue_only=true` query parameter is supplied.
