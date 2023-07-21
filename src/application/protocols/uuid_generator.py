from abc import ABC, abstractmethod


class IUUIDGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass
