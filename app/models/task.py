from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[datetime | None] = mapped_column(default=None)


def to_dict(self):
    return {
        "id": self.id,
        "title": self.title,
        "description": self.description,
        "completed_at": self.completed_at,
    }


@classmethod
def from_dict(cls, data):
    task = Task(
        title=data["title"],
        description=data["description"],
        completed_at=data["completed_at"],
    )
    return task


def get_task(self, id): 
    if id == self.id: 
        return True

