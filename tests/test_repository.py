import pytest
from src.repository import InMemoryTaskRepository, TaskNotFoundError
from src.models import TaskStatus

def test_add_task():
    repo = InMemoryTaskRepository()
    task = repo.add("Test Task", "Test Desc")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Desc"
    assert task.status == TaskStatus.PENDING

def test_get_all_tasks():
    repo = InMemoryTaskRepository()
    repo.add("Task 1")
    repo.add("Task 2")
    tasks = repo.get_all()
    assert len(tasks) == 2

def test_get_by_id():
    repo = InMemoryTaskRepository()
    task = repo.add("Task 1")
    found = repo.get_by_id(task.id)
    assert found == task

def test_update_task():
    repo = InMemoryTaskRepository()
    task = repo.add("Old Title")
    repo.update(task.id, title="New Title")
    assert task.title == "New Title"

def test_delete_task():
    repo = InMemoryTaskRepository()
    task = repo.add("To Delete")
    repo.delete(task.id)
    assert len(repo.get_all()) == 0

def test_task_not_found():
    repo = InMemoryTaskRepository()
    with pytest.raises(TaskNotFoundError):
        repo.delete(999)

def test_mark_status():
    repo = InMemoryTaskRepository()
    task = repo.add("Status Task")
    repo.mark_status(task.id, TaskStatus.DONE)
    assert task.status == TaskStatus.DONE
