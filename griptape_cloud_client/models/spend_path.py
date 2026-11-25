from enum import Enum


class SpendPath(str, Enum):
    CHAT = "CHAT"
    MODEL_PROXY = "MODEL_PROXY"
    REPORTED = "REPORTED"

    def __str__(self) -> str:
        return str(self.value)
