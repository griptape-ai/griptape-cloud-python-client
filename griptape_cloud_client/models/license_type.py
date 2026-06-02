from enum import Enum


class LicenseType(str, Enum):
    HEADLESS = "HEADLESS"
    INTERACTIVE = "INTERACTIVE"

    def __str__(self) -> str:
        return str(self.value)
