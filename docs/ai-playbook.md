# AI Playbook

## When I reach for AI first
- Generating boilerplate Python code for FastAPI Pydantic schemas and Pytest test structures.
- Writing initial documentation, docstrings, and markdown logs.
- Explaining complex error stack traces during Pytest failures or dependency issues.

## When I do not reach for AI first
- Designing overall core system architecture and in-memory data structures (`tasks_db`).
- Writing critical security configurations, container execution permissions, and input validation bounds.
- Defining project boundaries and core assignment business logic rules.

## My non-negotiables
- Never paste raw production secrets, tokens, or `.env` contents into AI models.
- All AI-generated code must be manually reviewed and tested locally before committing.
- Do not accept AI suggestions that bypass existing unit tests or security standards.

## My review rules
- Line-by-line check on all imports and logic changes proposed by AI.
- Validate that suggested code adheres strictly to Python/FastAPI best practices.
- Run `pytest` locally to confirm 100% test pass rate after applying any AI code.

## What I am still figuring out
- Optimizing prompt engineering strategies for complex edge-case bug resolution.
- Balancing automated AI security scanning tools with manual security auditing.

## Decision Card
- **New Feature:** Use AI assistants to outline Pydantic schemas and generate initial unit tests.
- **Code Review:** Use AI for syntax checks and formatting, followed by manual logic verification.
- **Debugging:** Paste non-sensitive stack traces into AI to diagnose FastAPI or Pytest errors.
- **Infrastructure:** Use AI to draft basic Dockerfile and GitHub Actions workflow templates.
- **Never-Paste:** API Keys, passwords, secret tokens, `.env` files, and private identity data.
- **Rule:** Every line of AI code must be tested via local Pytest before merging into the main repository.
