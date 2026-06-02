from enum import Enum


class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    RELEASED = "RELEASED"

    def __str__(self) -> str:
        return str(self.value)
