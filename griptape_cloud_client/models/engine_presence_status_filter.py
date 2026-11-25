from enum import Enum


class EnginePresenceStatusFilter(str, Enum):
    ALL = "ALL"
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"

    def __str__(self) -> str:
        return str(self.value)
