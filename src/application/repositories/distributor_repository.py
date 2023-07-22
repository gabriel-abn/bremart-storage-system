from abc import abstractmethod

from src.application.repositories.common.relational_repository import (
    RelationalRepository,
)
from src.domain.entities.distributor import Distributor, DistributorProps


class IDistributorRepository(RelationalRepository):
    @abstractmethod
    async def create(self, distributor: Distributor) -> dict[{"id": int}]:
        pass

    @abstractmethod
    async def update(self, distributor: Distributor) -> dict[{"id": int}]:
        pass

    @abstractmethod
    async def find_by_cnpj(self, cnpj: str) -> DistributorProps:
        pass

    @abstractmethod
    async def find_all(self) -> list[DistributorProps]:
        pass
