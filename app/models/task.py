from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from datetime import datetime


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[datetime | None] = mapped_column(default=None)
    is_complete = False
    goal_id: Mapped[int | None] = mapped_column(ForeignKey("goal.id"))
    goal: Mapped["Goal | None"] = relationship(back_populates="tasks")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            # "completed_at": self.completed_at,
            "is_complete": True if self.completed_at else False,
        }

    @classmethod
    def from_dict(cls, task_data):
        # data = cls.validate_attributes(cls, task_data)

        task = cls(
            title=task_data["title"],
            description=task_data["description"],
            completed_at=task_data.get("completed_at"),
            is_complete=True if task_data.get("completed_at") else False,
        )
        return task
