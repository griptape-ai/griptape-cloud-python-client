from enum import Enum


class CreditRateKind(str, Enum):
    DECLARED = "declared"
    LIST = "list"
    NEGOTIATED = "negotiated"
    PROMO = "promo"

    def __str__(self) -> str:
        return str(self.value)
