import pytest
from todo_lib.service import TodoService


def test_delete_existing_item(temp_db_path):
    """Test deleting an existing todo item."""
    service = TodoService(str(temp_db_path))

    todo_id = service.add_todo("Test task")

    result = service.delete_todo(todo_id)
    assert result is True

    todo = service._storage.get_todo_by_id(todo_id)
    assert todo is None


def test_delete_invalid_id(temp_db_path):
    """Test deleting a non-existent todo item."""
    service = TodoService(str(temp_db_path))

    result = service.delete_todo(999)
    assert result is False