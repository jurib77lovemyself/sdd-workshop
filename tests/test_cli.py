import os
from datetime import date
from pathlib import Path
from typer.testing import CliRunner
import cli.main as main


def test_cli_add_and_list_commands(temp_db_path, monkeypatch):
    """Test the CLI add and list commands using a temporary SQLite database."""
    monkeypatch.setenv("TODO_DB_PATH", str(temp_db_path))
    runner = CliRunner()

    add_result = runner.invoke(main.app, ["add", "CLI task", "--due", "2026-05-10", "--priority", "high"])
    assert add_result.exit_code == 0
    assert "added with ID" in add_result.stdout

    list_result = runner.invoke(main.app, ["list"])
    assert list_result.exit_code == 0
    assert "CLI task" in list_result.stdout
    assert "(high)" in list_result.stdout
    assert "Due: 2026-05-10" in list_result.stdout


def test_cli_done_and_delete_commands(temp_db_path, monkeypatch):
    """Test the CLI done and delete commands for a todo item."""
    monkeypatch.setenv("TODO_DB_PATH", str(temp_db_path))
    runner = CliRunner()

    add_result = runner.invoke(main.app, ["add", "Task to complete"])
    assert add_result.exit_code == 0
    assert "added with ID" in add_result.stdout

    # Extract created ID from output
    todo_id = int(add_result.stdout.strip().split()[-1])

    done_result = runner.invoke(main.app, ["done", str(todo_id)])
    assert done_result.exit_code == 0
    assert f"Todo item {todo_id} marked as done." in done_result.stdout

    delete_result = runner.invoke(main.app, ["delete", str(todo_id)])
    assert delete_result.exit_code == 0
    assert f"Todo item {todo_id} deleted." in delete_result.stdout

    # Verify deletion via list command
    list_result = runner.invoke(main.app, ["list"])
    assert list_result.exit_code == 0
    assert "No todos found." in list_result.stdout
