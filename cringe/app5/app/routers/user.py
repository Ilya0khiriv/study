from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=["user"])

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models.user import User
from app.models.task import Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if not tasks:
        return {'status_code': status.HTTP_404_NOT_FOUND, 'transaction': 'Tasks not found'}

    return tasks

@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    users = db.scalars(select(User).where(User.id == user_id)).all()

    if users:
        return users

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_category: CreateUser):
    user = db.scalars(select(User).where(User.username == create_category.username)).first()
    if user:
        return {'status_code': status.HTTP_409_CONFLICT, 'transaction': 'User exists already'}

    db.execute(insert(User).values(
        username=create_category.username,
        firstname=create_category.firstname,
        lastname=create_category.lastname,
        slug=create_category.username.lower(),
        age=create_category.age
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], create_category: UpdateUser, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))

    if not user:
        return {'status_code': status.HTTP_404_NOT_FOUND, 'transaction': 'User not found'}

    db.execute(update(User).where(User.id == user_id).values(
        firstname=create_category.firstname,
        lastname=create_category.lastname,
        age=create_category.age
    ))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))


    if not user:
        return {'status_code': status.HTTP_404_NOT_FOUND, 'transaction': 'User not found'}

    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User deletion is successful!'}
