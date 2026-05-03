#!/usr/bin/env python3
"""
Quickstart verification script for Todo CLI app.
This script demonstrates all 4 main CLI commands.
"""

import subprocess
import sys
import os

def run_command(cmd):
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0

def main():
    print("Todo CLI Quickstart Verification")
    print("=" * 40)

    # Add a todo
    run_command("uv run todo add \"Learn Python\" --priority high")

    # List todos
    run_command("uv run todo list")

    # Mark as done
    run_command("uv run todo done 1")

    # List again
    run_command("uv run todo list")

    # Delete
    run_command("uv run todo delete 1")

    # Final list
    run_command("uv run todo list")

    print("Verification complete!")

if __name__ == "__main__":
    main()