import pytest
from datetime import date
from todo_lib.service import TodoService


def test_add_todo_with_title_only(temp_db_path):
    """Test adding a todo item with title only."""
    service = TodoService(str(temp_db_path))

    todo_id = service.add_todo("Test task")

    assert todo_id == 1

    # Verify the todo was created correctly
    todo = service._storage.get_todo_by_id(1)  # Access storage for verification
    assert todo.title == "Test task"
    assert todo.description is None
    assert todo.due_date is None
    assert todo.priority is None
    assert not todo.completed


def test_add_todo_with_all_fields(temp_db_path):
    """Test adding a todo item with all optional fields."""
    service = TodoService(str(temp_db_path))

    due_date = date(2026, 5, 10)
    todo_id = service.add_todo("Test task", due_date=due_date, priority="high")

    assert todo_id == 1

    todo = service._storage.get_todo_by_id(1)
    assert todo.title == "Test task"
    assert todo.due_date == due_date
    assert todo.priority == "high"


def test_add_todo_missing_title_raises_error(temp_db_path):
    """Test that adding a todo without title raises an error."""
    service = TodoService(str(temp_db_path))

    with pytest.raises(ValueError, match="Title is required"):
        service.add_todo("")