from enum import Enum


class BudgetScopeType(str, Enum):
    LICENSE = "LICENSE"
    LICENSE_GROUP = "LICENSE_GROUP"
    ORG = "ORG"
    TAG = "TAG"

    def __str__(self) -> str:
        return str(self.value)
