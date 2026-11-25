from enum import Enum


class IntegrationType(str, Enum):
    SLACK = "slack"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
