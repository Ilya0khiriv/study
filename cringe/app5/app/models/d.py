from app.backend.db import engine, Base
from app.models.user import User
from app.models.task import Task
from sqlalchemy.schema import CreateTable

# Создание таблиц в базе данных
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))