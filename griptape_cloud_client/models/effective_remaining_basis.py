from enum import Enum


class EffectiveRemainingBasis(str, Enum):
    WORST_CASE = "worst_case"

    def __str__(self) -> str:
        return str(self.value)
