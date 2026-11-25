from enum import Enum


class Entitlement(str, Enum):
    ENTERPRISE = "ENTERPRISE"
    EXPIRED = "EXPIRED"
    FREE = "FREE"
    PROFESSIONAL = "PROFESSIONAL"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
