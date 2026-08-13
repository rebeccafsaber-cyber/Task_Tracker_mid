
# Architectural Decision Record (ADR)

## Title
Architectural Decisions for Status Transition Validation and Task Filtering Features

## Status
Accepted

## Context
During the mid-course project implementation, we needed to handle two core feature requirements:
1. Validating status transitions to prevent invalid task state flows (e.g., transitioning directly from `canceled` or `todo` to `done` without proper validation).
2. Allowing users to filter tasks based on specific attributes like tags and overdue status.

## Decision

### 1. Enum-Based Status Transition Validation
We decided to define task statuses using a Python `Enum` (`TaskStatus`) and manage transition logic using a pre-defined mapping table (`ALLOWED_TRANSITIONS`).
- Validation is enforced at the controller level during `PUT /tasks/{id}` requests.
- Invalid state transitions trigger an HTTP `400 Bad Request` response.

### 2. Query Parameter Filtering
We decided to implement task filtering (`overdue` and `tag`) using optional query parameters within the `GET /tasks` endpoint.
- Calculations for overdue items compare the `due_date` field against `date.today()` dynamically.
- Filtering is executed using in-memory list comprehensions to maintain high API efficiency and standard REST compliance.

## Consequences

### Positive
- **Data Consistency:** Prevents task state corruption by strictly enforcing allowed transitions.
- **Clean REST API:** Using standard query parameters (`?overdue=true&tag=work`) maintains intuitive client integration.
- **Maintainability:** Transitions are defined centrally in the dictionary map, making rules easy to modify in the future.

### Negative
- **In-Memory Limitations:** In-memory status transition checks and filtering need to be migrated to SQL/ORM queries when scaling to a real database.
