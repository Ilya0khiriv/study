from fastapi import APIRouter
router = APIRouter(prefix='/task', tags=["task"])

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models.task import Task
from app.models.user import User
from app.schemas import CreateUser, UpdateUser, CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id)).all()

    if task:
        return task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task_: CreateTask):
    user = db.scalars(select(User).where(User.id == create_task_.user_id)).first()

    if not user:
        return {'status_code': status.HTTP_404_NOT_FOUND, 'transaction': 'User was not found'}

    db.execute(insert(Task).values(
        title=create_task_.title,
        user_id=create_task_.user_id,
        content=create_task_.content,
        priority=create_task_.priority,
        slug=create_task_.title.lower()

    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], create_category: UpdateTask, task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))

    if not task:
        return {'status_code': status.HTTP_404_NOT_FOUND, 'transaction': 'Task not found'}

    db.execute(update(Task).where(Task.id == task_id).values(
        title=create_category.title,
        user_id=create_category.user_id,
        content=create_category.content,
        priority=create_category.priority,
        completed=create_category.completed
    ))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))

    if not task:
        return {'status_code': status.HTTP_404_NOT_FOUND, 'transaction': 'Task not found'}

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deletion is successful!'}
