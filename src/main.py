from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Модель задачи
class Task(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

# Хранилище для задач (в памяти)
tasks: List[Task] = []

# Главная страница
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в To-Do API"}

# Получить список всех задач
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Получить задачу по ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

# Добавить новую задачу
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    for t in tasks:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="ID уже существует")
    tasks.append(task)
    return task

# Обновить существующую задачу
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Задача не найдена")

# Удалить задачу
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")