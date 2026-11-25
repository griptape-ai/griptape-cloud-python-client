from enum import Enum


class LicenseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"

    def __str__(self) -> str:
        return str(self.value)
