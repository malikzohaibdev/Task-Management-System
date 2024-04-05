from fastapi import FastAPI, HTTPException
from .schemas import TaskCreate, TaskResponse
from typing import List
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.config.settings')
django.setup()

from tasks.models import Task
from django.contrib.auth.models import User

app = FastAPI()


@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    
    user = User.objects.filter(username=task.assigned_to).first()
    if not user:
        raise HTTPException(status_code=404, detail="Assigned user not found")
    
    db_task = Task.objects.create(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        priority=task.priority,
        status=task.status,
        assigned_to=user
    )
    return db_task

@app.get("/tasks/", response_model=List[TaskResponse])
def read_tasks():
    tasks = Task.objects.all()
    return list(tasks)


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskCreate):
    from django.contrib.auth.models import User
    user = User.objects.filter(username=task_update.assigned_to).first()
    if not user:
        raise HTTPException(status_code=404, detail="Assigned user not found")
    
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in task_update.dict().items():
        setattr(task, key, value)
    task.assigned_to = user
    task.save()
    return task

@app.delete("/tasks/{task_id}", response_model=None)
def delete_task(task_id: int):
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.delete()
    return {"message": "Task deleted successfully"}
