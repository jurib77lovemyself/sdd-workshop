import pytest
from todo_lib.storage import SQLiteStorage
from todo_lib.models import TodoItem


def test_storage_operations(temp_db_path):
    """Integration test for SQLiteStorage operations."""
    storage = SQLiteStorage(str(temp_db_path))

    # Test create
    todo_id = storage.create_todo("Test Todo", "Description", None, "high")
    assert todo_id == 1

    # Test get by id
    todo = storage.get_todo_by_id(1)
    assert todo is not None
    assert todo.title == "Test Todo"
    assert todo.description == "Description"
    assert todo.priority == "high"
    assert not todo.completed

    # Test update
    storage.update_todo(1, completed=True, title="Updated Todo")
    todo = storage.get_todo_by_id(1)
    assert todo.title == "Updated Todo"
    assert todo.completed

    # Test get all
    todos = storage.get_all_todos()
    assert len(todos) == 1

    # Test filter by completion
    pending = storage.filter_by_completion(False)
    assert len(pending) == 0
    completed = storage.filter_by_completion(True)
    assert len(completed) == 1

    # Test filter by priority
    high_priority = storage.filter_by_priority("high")
    assert len(high_priority) == 1
    low_priority = storage.filter_by_priority("low")
    assert len(low_priority) == 0

    # Test delete
    assert storage.delete_todo(1)
    assert storage.get_todo_by_id(1) is None
    assert not storage.delete_todo(999)  # Non-existent ID