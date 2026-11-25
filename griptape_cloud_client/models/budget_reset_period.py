from enum import Enum


class BudgetResetPeriod(str, Enum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"
    YEARLY = "YEARLY"

    def __str__(self) -> str:
        return str(self.value)
