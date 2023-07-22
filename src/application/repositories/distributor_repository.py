from abc import ABC, abstractmethod

from src.domain.entities.distributor import Distributor, DistributorProps


class IDistributorRepository(ABC):
    @abstractmethod
    async def create(self, distributor: Distributor) -> dict[{"id": int}]:
        pass

    @abstractmethod
    async def update(self, distributor: Distributor) -> DistributorProps:
        pass

    @abstractmethod
    async def find_one(self, cnpj: str) -> DistributorProps:
        pass
