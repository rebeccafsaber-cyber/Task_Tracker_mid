
from fastapi.testclient import TestClient
import sys
import os

# Add backend directory to path to import main app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing FastAPI endpoint",
            "due_date": "2026-12-31"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_overdue_filter():
    response = client.post(
        "/tasks/",
        json={
            "title": "Overdue Test Task",
            "description": "Testing overdue filter",
            "due_date": "2020-01-01"
        }
    )

    assert response.status_code == 201

    response = client.get("/tasks/?overdue=true")

    assert response.status_code == 200

    tasks = response.json()

    assert any(task["title"] == "Overdue Test Task" for task in tasks)


def test_tag_filter():
    response = client.post(
        "/tasks/",
        json={
            "title": "Tagged Test Task",
            "description": "Testing tag filter",
            "due_date": "2026-12-31",
            "tags": ["school"]
        }
    )

    assert response.status_code == 201

    response = client.get("/tasks/?tag=school")

    assert response.status_code == 200

    tasks = response.json()

    assert any(task["title"] == "Tagged Test Task" for task in tasks)