from datetime import date
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Task Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELED = "canceled"



ALLOWED_TRANSITIONS = {
    TaskStatus.TODO: [TaskStatus.IN_PROGRESS, TaskStatus.CANCELED],
    TaskStatus.IN_PROGRESS: [TaskStatus.DONE, TaskStatus.TODO, TaskStatus.CANCELED],
    TaskStatus.DONE: [TaskStatus.IN_PROGRESS],
    TaskStatus.CANCELED: [TaskStatus.TODO],
}



class TodoItem(BaseModel):
    id: int
    title: str
    notes: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    due_date: Optional[date] = None
    tags: List[str] = Field(default_factory=list)



storage_db: List[TodoItem] = []


@app.get("/")
def home():
    return {"message": "Welcome to the Task Management API"}


@app.get("/tasks", response_model=List[TodoItem])
def fetch_tasks(overdue: Optional[bool] = None, tag: Optional[str] = None):
    filtered_list = storage_db
    current_date = date.today()

    if overdue is not None:
        if overdue:
            filtered_list = [
                t
                for t in filtered_list
                if t.due_date and t.due_date < current_date and t.status != TaskStatus.DONE
            ]
        else:
            filtered_list = [
                t
                for t in filtered_list
                if not t.due_date or t.due_date >= current_date or t.status == TaskStatus.DONE
            ]

    if tag:
        filtered_list = [
            t for t in filtered_list if tag in t.tags
        ]

    return filtered_list


@app.post("/tasks", response_model=TodoItem)
def add_task(new_task: TodoItem):
    for existing in storage_db:
        if existing.id == new_task.id:
            raise HTTPException(
                status_code=400, detail="Task ID already exists"
            )
    storage_db.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=TodoItem)
def modify_task(task_id: int, updated_task: TodoItem):
    for position, item in enumerate(storage_db):
        if item.id == task_id:
            current_status = item.status
            new_status = updated_task.status

            
            if current_status != new_status:
                allowed_next = ALLOWED_TRANSITIONS.get(current_status, [])
                if new_status not in allowed_next:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Cannot transition status from '{current_status.value}' to '{new_status.value}'"
                    )

            storage_db[position] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    for position, item in enumerate(storage_db):
        if item.id == task_id:
            storage_db.pop(position)
            return {"message": "Task successfully removed"}
    raise HTTPException(status_code=404, detail="Task not found")
