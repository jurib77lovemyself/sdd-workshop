from .storage import SQLiteStorage


class TodoService:
    def __init__(self, db_path: str):
        self._storage = SQLiteStorage(db_path)

    def add_todo(self, title: str, description: str = None, due_date = None, priority: str = None):
        """Add a new todo item.

        Args:
            title: The title of the todo item (required)
            description: Optional description
            due_date: Optional due date (date object)
            priority: Optional priority ('high', 'medium', 'low')

        Returns:
            The ID of the created todo item

        Raises:
            ValueError: If title is empty or priority is invalid
        """
        if not title or not title.strip():
            raise ValueError("Title is required")

        if len(title) > 200:
            raise ValueError("Title must be 200 characters or less")

        if priority and priority not in ["high", "medium", "low"]:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")

        return self._storage.create_todo(title, description, due_date, priority)

    def list_todos(self, filter_status=None, filter_priority=None):
        """List todos with optional filters.

        Args:
            filter_status: 'done' or 'pending' to filter by completion
            filter_priority: 'high', 'medium', 'low' to filter by priority

        Returns:
            List of TodoItem objects matching the filters
        """
        if filter_status and filter_priority:
            # Combined filter
            status_completed = filter_status == "done"
            todos = self._storage.filter_by_completion(status_completed)
            return [t for t in todos if t.priority == filter_priority]
        elif filter_status:
            status_completed = filter_status == "done"
            return self._storage.filter_by_completion(status_completed)
        elif filter_priority:
            return self._storage.filter_by_priority(filter_priority)
        else:
            return self._storage.get_all_todos()

    def mark_done(self, todo_id: int):
        """Mark a todo item as completed.

        Args:
            todo_id: The ID of the todo item to mark as done

        Returns:
            True if the item was found and marked, False otherwise
        """
        todo = self._storage.get_todo_by_id(todo_id)
        if todo:
            self._storage.update_todo(todo_id, completed=True)
            return True
        return False

    def delete_todo(self, todo_id: int):
        """Delete a todo item.

        Args:
            todo_id: The ID of the todo item to delete

        Returns:
            True if the item was found and deleted, False otherwise
        """
        return self._storage.delete_todo(todo_id)