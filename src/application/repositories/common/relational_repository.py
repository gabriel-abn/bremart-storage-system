from abc import ABC, abstractmethod

from src.application.repositories.common.relational_database import RelationalDatabase


class RelationalRepository(ABC):
    @abstractmethod
    def __init__(self, relational_db: RelationalDatabase) -> None:
        pass
