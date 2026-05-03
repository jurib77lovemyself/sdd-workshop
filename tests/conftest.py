import tempfile
import pytest
from pathlib import Path
from todo_lib.storage import SQLiteStorage # Import SQLiteStorage

@pytest.fixture
def temp_db_path():
    """Fixture providing a temporary SQLite database file path for testing."""
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        temp_path = Path(f.name)

    # Yield the path, then ensure connection is closed before unlinking
    yield temp_path
    
    # Close any active connections to the database file before deleting
    # This assumes SQLiteStorage is the primary way to interact with the DB in tests
    # If other connections exist, they would also need to be closed.
    storage = SQLiteStorage(db_path=temp_path)
    storage.close()

    # Cleanup after test
    temp_path.unlink(missing_ok=True)