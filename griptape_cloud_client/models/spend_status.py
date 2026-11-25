from enum import Enum


class SpendStatus(str, Enum):
    BLOCKED = "BLOCKED"
    PENDING = "PENDING"
    RELEASED = "RELEASED"
    SETTLED = "SETTLED"

    def __str__(self) -> str:
        return str(self.value)
