from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    assignee: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    assignee: str | None = None
    status: TaskStatus | None = None


class TaskOut(BaseModel):
    id: int
    title: str
    assignee: str | None
    status: TaskStatus
    created_at: datetime
