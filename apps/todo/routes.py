from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from starlette import status

from apps.todo.models import Task

router = APIRouter(tags=["todo"], prefix="/todo")


@router.get("/tasks", status_code=status.HTTP_200_OK)
async def get_tasks() -> List[Task]:
    tasks = await Task.find_all().to_list()
    return tasks


@router.post("/tasks/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    await task.create()

    return {"message": "Task has been successfully created."}


@router.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def retrieve_task(task_id: UUID) -> Task:
    task = await Task.get(task_id)
    return task


@router.patch("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(updated_task: Task, task_id: UUID):
    task = await Task.get(task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    task.name = updated_task.name
    task.description = updated_task.description
    task.status = updated_task.status
    task.date_updated = datetime.now()
    await task.save()

    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_410_GONE)
async def delete_task(task_id: UUID):
    task = await Task.get(task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    await task.delete()

    return {"message": "Task was successfully deleted."}
