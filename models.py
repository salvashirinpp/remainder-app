from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime

@dataclass
class Reminder:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    date: str = ""    # format: YYYY-MM-DD
    time: str = ""    # format: HH:MM
    status: str = "Pending"

    def is_due(self) -> bool:
        """Check if the reminder is due."""
        reminder_datetime = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
        return datetime.now() >= reminder_datetime
