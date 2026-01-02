from typing import List, Optional
from src.models import Task, TaskStatus

class TaskNotFoundError(Exception):
    def __init__(self, task_id: int):
        super().__init__(f"Task with ID {task_id} not found.")

class InMemoryTaskRepository:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, title: str, description: str = "") -> Task:
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all(self, status: Optional[TaskStatus] = None) -> List[Task]:
        if status:
            return [t for t in self._tasks.values() if t.status == status]
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        task = self.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(task_id)
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        return task

    def delete(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        raise TaskNotFoundError(task_id)

    def mark_status(self, task_id: int, status: TaskStatus) -> Task:
        task = self.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(task_id)
        task.status = status
        return task
