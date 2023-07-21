from abc import ABC, abstractmethod


class ICrypter(ABC):
    @abstractmethod
    def encrypt(self, value: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, value: str) -> str:
        pass
