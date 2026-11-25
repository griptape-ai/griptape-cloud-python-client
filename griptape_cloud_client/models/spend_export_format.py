from enum import Enum


class SpendExportFormat(str, Enum):
    CSV = "csv"
    JSONL = "jsonl"

    def __str__(self) -> str:
        return str(self.value)
