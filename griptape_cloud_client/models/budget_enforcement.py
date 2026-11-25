from enum import Enum


class BudgetEnforcement(str, Enum):
    HARD = "HARD"
    SOFT = "SOFT"

    def __str__(self) -> str:
        return str(self.value)
