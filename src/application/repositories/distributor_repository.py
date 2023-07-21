from abc import ABC, abstractmethod

from src.domain.entities.distributor import Distributor, DistributorProps


class IDistributorRepository(ABC):
    @abstractmethod
    def create(self, distributor: Distributor) -> dict[{"id": int}]:
        pass

    @abstractmethod
    def update(self, distributor: Distributor) -> DistributorProps:
        pass
