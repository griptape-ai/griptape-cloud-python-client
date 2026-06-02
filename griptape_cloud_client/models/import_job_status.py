from enum import Enum


class ImportJobStatus(str, Enum):
    CANCELLED = "CANCELLED"
    CREATED = "CREATED"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
