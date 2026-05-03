import pytest
from todo_lib.service import TodoService


def test_list_todos_no_filters(temp_db_path):
    """Test listing all todos without filters."""
    service = TodoService(str(temp_db_path))

    # Add some test todos
    service.add_todo("Task 1", priority="high")
    service.add_todo("Task 2", priority="low")
    service.add_todo("Task 3")

    todos = service.list_todos()
    assert len(todos) == 3
    assert todos[0].title == "Task 1"
    assert todos[1].title == "Task 2"
    assert todos[2].title == "Task 3"


def test_list_todos_filter_by_status(temp_db_path):
    """Test filtering todos by completion status."""
    service = TodoService(str(temp_db_path))

    service.add_todo("Task 1")
    service.add_todo("Task 2")

    # Mark first task as done
    todos = service.list_todos()
    service._storage.update_todo(todos[0].id, completed=True)

    pending = service.list_todos(filter_status="pending")
    assert len(pending) == 1
    assert pending[0].title == "Task 2"
    assert not pending[0].completed

    done = service.list_todos(filter_status="done")
    assert len(done) == 1
    assert done[0].title == "Task 1"
    assert done[0].completed


def test_list_todos_filter_by_priority(temp_db_path):
    """Test filtering todos by priority."""
    service = TodoService(str(temp_db_path))

    service.add_todo("High Task", priority="high")
    service.add_todo("Low Task", priority="low")
    service.add_todo("No Priority Task")

    high_priority = service.list_todos(filter_priority="high")
    assert len(high_priority) == 1
    assert high_priority[0].title == "High Task"

    low_priority = service.list_todos(filter_priority="low")
    assert len(low_priority) == 1
    assert low_priority[0].title == "Low Task"

    # No priority filter should return all
    all_todos = service.list_todos()
    assert len(all_todos) == 3


def test_list_todos_combined_filters(temp_db_path):
    """Test filtering todos by both status and priority."""
    service = TodoService(str(temp_db_path))

    service.add_todo("High Pending", priority="high")
    service.add_todo("High Done", priority="high")
    service.add_todo("Low Pending", priority="low")

    # Mark one high priority as done
    todos = service.list_todos(filter_priority="high")
    service._storage.update_todo(todos[1].id, completed=True)

    # Filter for pending high priority
    pending_high = service.list_todos(filter_status="pending", filter_priority="high")
    assert len(pending_high) == 1
    assert pending_high[0].title == "High Pending"
    assert pending_high[0].priority == "high"
    assert not pending_high[0].completed