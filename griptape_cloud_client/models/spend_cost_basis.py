from enum import Enum


class SpendCostBasis(str, Enum):
    BILLED = "BILLED"
    DECLARED = "DECLARED"
    ESTIMATED = "ESTIMATED"

    def __str__(self) -> str:
        return str(self.value)
