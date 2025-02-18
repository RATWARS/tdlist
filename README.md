# To-Do API

Этот проект представляет собой простой To-Do API, созданный с использованием FastAPI. API позволяет создавать, просматривать, обновлять и удалять задачи.

## 🚀 Функциональность
- **Просмотр всех задач:** Получение списка всех задач.
- **Создание новой задачи:** Добавление задачи с уникальным ID.
- **Просмотр задачи по ID:** Получение информации о конкретной задаче.
- **Обновление задачи:** Редактирование данных о задаче.
- **Удаление задачи:** Удаление задачи по её ID.

## 📋 Требования
Перед началом убедитесь, что у вас установлены:
- Python 3.7+
- pip (менеджер пакетов Python)

## 🛠️ Настройка окружения

1. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   ```

2. **Активируйте виртуальное окружение:**
   - **Для Linux/MacOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Для Windows:**
     ```cmd
     venv\Scripts\activate
     ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Запуск проекта

1. Запустите сервер FastAPI с помощью Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. Сервер будет доступен по адресу:
   ```
   http://127.0.0.1:8000
   ```
   Либо:
   ```
   http://localhost:8000
   ```
## 📄 Работа с API через Swagger UI
FastAPI автоматически предоставляет интерактивную документацию. Чтобы использовать её:

1. Перейдите по адресу:
   ```
   http://127.0.0.1:8000/docs
   ```
2. Вы увидите интерфейс Swagger UI, где можно:
   - Просматривать все доступные эндпоинты.
   - Отправлять запросы (GET, POST, PUT, DELETE) напрямую из браузера.

## 🧹 Завершение работы
Для отключения сервера:
```bash
Ctrl+C
```
Для отключения окружения:
```bash
deactivate
```
После завершения работы вы можете удалить виртуальное окружение:
```bash
rm -rf venv  # Для Linux/MacOS
rd /s /q venv  # Для Windows
```