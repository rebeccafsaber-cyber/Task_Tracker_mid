## Final Project

### Overview
This repository contains the complete implementation for the FastAPI Task Tracker project submission.

### Key Features
- Full CRUD task operations with auto-incrementing IDs.
- Advanced query filtering by `tag` and `overdue_only` status.
- Pydantic schema validation including `status`, `tags`, and `due_date`.
- Complete automated unit testing suite using `pytest` verifying all endpoints (including root `/`).

### How to Run & Test
1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
