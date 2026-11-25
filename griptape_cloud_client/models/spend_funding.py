from enum import Enum


class SpendFunding(str, Enum):
    CUSTOMER_ACCOUNT = "CUSTOMER_ACCOUNT"
    GRIPTAPE_CREDITS = "GRIPTAPE_CREDITS"

    def __str__(self) -> str:
        return str(self.value)
