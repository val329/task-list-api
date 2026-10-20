from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[datetime | None] = mapped_column(default=None)
    is_complete = False


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            # "completed_at": self.completed_at,
            "is_complete": True if self.completed_at else False
        }


    @classmethod
    def from_dict(cls, data):
        data = cls.validate_attributes(cls, data)

        task = cls(
            title=data.get("title"),
            description=data.get("description"),
            completed_at=data.get("completed_at"), 
            is_complete=True if data.get("completed_at") else False
        )
        return task
    

    def validate_attributes(self, data):
        REQUIRED_ATTRIBUTES = ["title", "description"]

        for attr in REQUIRED_ATTRIBUTES: 
            if not data.get(attr):
                raise KeyError(f"details: Invalid data, missing {attr}")

        return data


        

        

