import pytest
from todo_lib.service import TodoService


def test_mark_done_pending_item(temp_db_path):
    """Test marking a pending todo as done."""
    service = TodoService(str(temp_db_path))

    todo_id = service.add_todo("Test task")

    result = service.mark_done(todo_id)
    assert result is True

    todo = service._storage.get_todo_by_id(todo_id)
    assert todo.completed


def test_mark_done_already_completed_item(temp_db_path):
    """Test marking an already completed todo as done (idempotent)."""
    service = TodoService(str(temp_db_path))

    todo_id = service.add_todo("Test task")

    # Mark as done first time
    service.mark_done(todo_id)

    # Mark as done second time
    result = service.mark_done(todo_id)
    assert result is True

    todo = service._storage.get_todo_by_id(todo_id)
    assert todo.completed


def test_mark_done_invalid_id(temp_db_path):
    """Test marking a non-existent todo as done."""
    service = TodoService(str(temp_db_path))

    result = service.mark_done(999)
    assert result is False