from __future__ import annotations

from datetime import datetime, timezone

from app.errors import NotFoundError
from app.schemas import TaskCreate, TaskOut, TaskStatus, TaskUpdate


class TaskRepository:
    """Stockage en mémoire, volontairement simple : la persistance arrive au Module 5."""

    def __init__(self) -> None:
        self._tasks: dict[int, TaskOut] = {}
        self._next_id = 1

    def list(self, status: TaskStatus | None = None) -> list[TaskOut]:
        tasks = list(self._tasks.values())
        if status is not None:
            tasks = [t for t in tasks if t.status == status]
        return sorted(tasks, key=lambda t: t.id)

    def get(self, task_id: int) -> TaskOut:
        try:
            return self._tasks[task_id]
        except KeyError:
            raise NotFoundError(f"Tâche {task_id} introuvable") from None

    def create(self, data: TaskCreate) -> TaskOut:
        task = TaskOut(
            id=self._next_id,
            title=data.title,
            assignee=data.assignee,
            status=TaskStatus.TODO,
            created_at=datetime.now(timezone.utc),
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def update(self, task_id: int, data: TaskUpdate) -> TaskOut:
        current = self.get(task_id)
        updated = current.model_copy(update=data.model_dump(exclude_none=True))
        self._tasks[task_id] = updated
        return updated

    def clear(self) -> None:
        self._tasks.clear()
        self._next_id = 1


repository = TaskRepository()
