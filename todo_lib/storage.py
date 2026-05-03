from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.pool import NullPool
from .models import Base, TodoItem


class SQLiteStorage:
    def __init__(self, db_path: str):
        self.engine = create_engine(
            f"sqlite:///{db_path}",
            connect_args={"check_same_thread": False},
            poolclass=NullPool,
        )
        Base.metadata.create_all(self.engine)

    def close(self):
        """Close the database engine and release SQLite resources."""
        self.engine.dispose()

    def create_todo(self, title: str, description: str = None, due_date = None, priority: str = None):
        with Session(self.engine) as session:
            todo = TodoItem(
                title=title,
                description=description,
                due_date=due_date,
                priority=priority
            )
            session.add(todo)
            session.commit()
            return todo.id

    def get_todo_by_id(self, todo_id: int):
        with Session(self.engine) as session:
            return session.get(TodoItem, todo_id)

    def get_all_todos(self):
        with Session(self.engine) as session:
            return list(session.scalars(select(TodoItem)).all())

    def update_todo(self, todo_id: int, **kwargs):
        with Session(self.engine) as session:
            stmt = update(TodoItem).where(TodoItem.id == todo_id).values(**kwargs)
            result = session.execute(stmt)
            session.commit()
            return result.rowcount > 0

    def delete_todo(self, todo_id: int):
        with Session(self.engine) as session:
            todo = session.get(TodoItem, todo_id)
            if todo:
                session.delete(todo)
                session.commit()
                return True
            return False

    def filter_by_completion(self, completed: bool):
        with Session(self.engine) as session:
            return list(session.scalars(
                select(TodoItem).where(TodoItem.completed == completed)
            ).all())

    def filter_by_priority(self, priority: str):
        with Session(self.engine) as session:
            return list(session.scalars(
                select(TodoItem).where(TodoItem.priority == priority)
            ).all())