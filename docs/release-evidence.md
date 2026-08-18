# Release Evidence

## Baseline
- **Branch:** `final-project`
- **Date:** 2026-08-18
- **Local Run Command:** `uvicorn app.main:app --reload`
- **Health Result:** `curl http://127.0.0.1:8000/` -> `200 OK` `{"message": "Welcome to Task Tracker API"}`
- **Frontend Check:** N/A (Backend API only / Verified swagger UI accessible at `http://127.0.0.1:8000/docs`)

## CI Evidence
- **Workflow File:** `.github/workflows/ci.yml`
- **Run Link:** https://github.com/rebeccafsaber-cyber/Task_Tracker_mid/actions/runs/16
- **Shortcut Check:** Passed (All tests and linting steps executed without `--skip` flags or bypassed triggers)

## Docker Evidence
- **Build Command:** `docker build -t task-tracker-api .`
- **Run Command:** `docker run -p 8000:8000 task-tracker-api`
- **Health Check:** `curl http://localhost:8000/` -> `200 OK`
- **Non-root Check:** `docker exec <container_id> whoami` -> Output: `appuser` (Non-root user verified)
- **No-baked-secrets Check:** Passed (Verified no API keys, credentials, or `.env` files hardcoded inside the Dockerfile or image layers)

## Documentation Claim-vs-Reality Log
| Claim | Reality | Status |
| :--- | :--- | :--- |
| API service starts on port 8000 | Verified application runs on port 8000 locally and inside Docker container | Matched |
| All core endpoint unit tests pass | Executed `pytest` suite; 100% tests passed with zero failures | Matched |
| Root `/` endpoint returns HTTP 200 | Sent GET request to `/`, observed `200 OK` with welcome JSON payload | Matched |
| Docker container runs with non-root privileges | Ran `whoami` inside container, confirmed execution under `appuser` | Matched |
