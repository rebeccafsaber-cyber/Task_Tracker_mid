from datetime import date
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


class TodoItem(BaseModel):
    task_id: int
    title: str
    notes: Optional[str] = None
    is_done: bool = False
    deadline: Optional[date] = None
    categories: List[str] = Field(default_factory=list)


# قاعدة بيانات مؤقتة بأسماء متغيرات مختلفة
storage_db: List[TodoItem] = []


@app.get("/")
def home():
    return {"message": "Welcome to the Task Management API"}


@app.get("/tasks", response_model=List[TodoItem])
def fetch_tasks(delayed: Optional[bool] = None, category: Optional[str] = None):
    filtered_list = storage_db
    current_date = date.today()

    if delayed is not None:
        if delayed:
            filtered_list = [
                t
                for t in filtered_list
                if t.deadline and t.deadline < current_date and not t.is_done
            ]
        else:
            filtered_list = [
                t
                for t in filtered_list
                if not t.deadline or t.deadline >= current_date or t.is_done
            ]

    if category:
        filtered_list = [
            t for t in filtered_list if category in t.categories
        ]

    return filtered_list


@app.post("/tasks", response_model=TodoItem)
def add_task(new_task: TodoItem):
    for existing in storage_db:
        if existing.task_id == new_task.task_id:
            raise HTTPException(
                status_code=400, detail="Task ID already exists"
            )
    storage_db.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=TodoItem)
def modify_task(task_id: int, updated_task: TodoItem):
    for position, item in enumerate(storage_db):
        if item.task_id == task_id:
            storage_db[position] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    for position, item in enumerate(storage_db):
        if item.task_id == task_id:
            storage_db.pop(position)
            return {"message": "Task successfully removed"}
    raise HTTPException(status_code=404, detail="Task not found")
