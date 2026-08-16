from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Task Management Service", version="2.0.0")

class TaskSchema(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: str = "pending"
    tags: List[str] = []
    due_date: Optional[str] = None
    completed: bool = False

storage: List[TaskSchema] = []
auto_increment_id: int = 0

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Management API"}

@app.get("/tasks", response_model=List[TaskSchema])
def fetch_all_tasks(
    tag: Optional[str] = Query(None, description="Filter tasks by tag"),
    overdue_only: bool = Query(False, description="Filter overdue tasks")
):
    results = storage

    if tag:
        results = [t for t in results if tag in t.tags]

    if overdue_only:
        today_str = datetime.now().strftime("%Y-%m-%d")
        results = [
            t for t in results 
            if t.due_date and t.due_date < today_str and not t.completed
        ]

    return results

@app.post("/tasks", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def insert_task(payload: TaskSchema):
    global auto_increment_id
    auto_increment_id += 1
    payload.id = auto_increment_id
    storage.append(payload)
    return payload

@app.get("/tasks/{task_id}", response_model=TaskSchema)
def fetch_task_by_id(task_id: int):
    matching_task = next((item for item in storage if item.id == task_id), None)
    if not matching_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return matching_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_by_id(task_id: int):
    global storage
    target_index = next((idx for idx, item in enumerate(storage) if item.id == task_id), None)
    if target_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    storage.pop(target_index)
    return
