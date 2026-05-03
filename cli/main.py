import os
import typer
from datetime import datetime
from pathlib import Path
from todo_lib.service import TodoService

app = typer.Typer()


def get_db_path():
    return os.getenv("TODO_DB_PATH", "todo.db")


@app.command("add")
def add_command(
    title: str = typer.Argument(..., help="The title of the todo item"),
    due: str = typer.Option(None, "--due", help="Due date in YYYY-MM-DD format"),
    priority: str = typer.Option(None, "--priority", help="Priority: high, medium, or low")
):
    """Add a new todo item."""
    try:
        service = TodoService(get_db_path())

        due_date = None
        if due:
            due_date = datetime.strptime(due, "%Y-%m-%d").date()

        todo_id = service.add_todo(title, due_date=due_date, priority=priority)

        typer.echo(f"Todo item '{title}' added with ID: {todo_id}")

    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command("list")
def list_command(
    filter_status: str = typer.Option(None, "--filter", help="Filter by status: done or pending"),
    priority: str = typer.Option(None, "--priority", help="Filter by priority: high, medium, or low")
):
    """List todo items with optional filters."""
    try:
        service = TodoService(get_db_path())
        todos = service.list_todos(filter_status=filter_status, filter_priority=priority)

        if not todos:
            typer.echo("No todos found.")
            return

        for todo in todos:
            status = "[X]" if todo.completed else "[ ]"
            pri = f" ({todo.priority})" if todo.priority else ""
            due = f" - Due: {todo.due_date}" if todo.due_date else ""
            typer.echo(f"{todo.id}. {status} {todo.title}{pri}{due}")

    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command("done")
def done_command(todo_id: int = typer.Argument(..., help="The ID of the todo item to mark as done")):
    """Mark a todo item as completed."""
    try:
        service = TodoService(get_db_path())

        if service.mark_done(todo_id):
            typer.echo(f"Todo item {todo_id} marked as done.")
        else:
            typer.echo(f"Todo item {todo_id} not found.", err=True)
            raise typer.Exit(1)

    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command("delete")
def delete_command(todo_id: int = typer.Argument(..., help="The ID of the todo item to delete")):
    """Delete a todo item."""
    try:
        service = TodoService(get_db_path())

        if service.delete_todo(todo_id):
            typer.echo(f"Todo item {todo_id} deleted.")
        else:
            typer.echo(f"Todo item {todo_id} not found.", err=True)
            raise typer.Exit(1)

    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()