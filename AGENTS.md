# Autonomous Agents Configuration - Task Tracker

## Agent Definitions

The following guidelines govern AI usage and automated code generation for the Task Tracker microservice.

### 1. Development & Refactoring Agent
- **Responsibility:** Assists with generating FastAPI endpoints, Pydantic schemas, and Pytest coverage within `backend/`.
- **Constraints:** Must not invent external files or dependencies. All code generated must be fully compatible with Python 3.9 and FastAPI standards.

### 2. Testing & Quality Guardrail Agent
- **Responsibility:** Verifies endpoint validity, handles status code assertions, and runs `flake8` linting checks.
- **Constraints:** Ensures all test functions remain synchronous where applicable and covers both success and edge cases (e.g., HTTP 404 responses).

## Non-Negotiable Development Rules
- Every endpoint added to `backend/main.py` must have an associated test in `tests/`.
- No hardcoded credentials, secret keys, or unconfigured middleware are allowed.
- AI-generated responses must accurately reflect existing repository structure.
