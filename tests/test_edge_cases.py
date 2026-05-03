import pytest
from datetime import date
from todo_lib.service import TodoService


def test_long_title_validation(temp_db_path):
    """Test that titles longer than 200 characters are rejected."""
    service = TodoService(str(temp_db_path))

    long_title = "A" * 201
    with pytest.raises(ValueError, match="Title must be 200 characters or less"):
        service.add_todo(long_title)


def test_empty_database_list(temp_db_path):
    """Test listing todos in an empty database."""
    service = TodoService(str(temp_db_path))

    todos = service.list_todos()
    assert todos == []


def test_past_due_date_handling(temp_db_path):
    """Test handling of past due dates."""
    service = TodoService(str(temp_db_path))

    past_date = date(2020, 1, 1)
    todo_id = service.add_todo("Past due task", due_date=past_date)

    todo = service._storage.get_todo_by_id(todo_id)
    assert todo.due_date == past_date