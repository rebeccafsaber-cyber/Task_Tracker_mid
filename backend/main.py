
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Task Tracker API", version="1.0.0")

class TaskItem(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks_db: List[TaskItem] = []
counter: int = 0

@app.get("/tasks", response_model=List[TaskItem])
def get_all_tasks():
    return tasks_db

@app.post("/tasks", response_model=TaskItem, status_code=status.HTTP_201_CREATED)
def create_new_task(task: TaskItem):
    global counter
    counter += 1
    task.id = counter
    tasks_db.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=TaskItem)
def get_task_by_id(task_id: int):
    for t in tasks_db:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(task_id: int):
    global tasks_db
    for index, t in enumerate(tasks_db):
        if t.id == task_id:
            tasks_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")
