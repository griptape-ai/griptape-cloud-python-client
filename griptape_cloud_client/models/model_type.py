from enum import Enum


class ModelType(str, Enum):
    CHAT = "chat"
    CLASSIFICATION = "classification"
    EMBEDDING = "embedding"
    IMAGE_GENERATION = "image_generation"
    RERANK = "rerank"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
