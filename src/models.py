from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class TaskStatus(Enum):
    PENDING = "Pending"
    DONE = "Done"

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat()
        }
