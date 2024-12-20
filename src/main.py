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