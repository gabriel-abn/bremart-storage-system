from abc import ABC, abstractmethod


class IDataValidation(ABC):
    @abstractmethod
    async def validate_cep(self, cep: str) -> bool:
        pass

    @abstractmethod
    async def validate_cnpj(self, cnpj: str) -> bool:
        pass
