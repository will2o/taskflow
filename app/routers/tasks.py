from __future__ import annotations

from fastapi import APIRouter, status

from app.repository import repository
from app.schemas import TaskCreate, TaskOut, TaskStatus, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskOut])
def list_tasks(status: TaskStatus | None = None) -> list[TaskOut]:
    return repository.list(status=status)


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate) -> TaskOut:
    return repository.create(data)


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int) -> TaskOut:
    return repository.get(task_id)


@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, data: TaskUpdate) -> TaskOut:
    return repository.update(task_id, data)
