from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class TaskStatus(str, Enum):
    PENDING = "pending"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Task(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    status: Optional[TaskStatus]
    date_created: datetime
    date_updated: datetime

    class Settings:
        name = 'tasks'

    class Config:
        schema_extra = {
            "name": "Setup fastapi crud with beani & mongodb",
            "status": TaskStatus.ONGOING,
            "date_created": datetime.utcnow(),
            "date_updated": datetime.utcnow()
        }
