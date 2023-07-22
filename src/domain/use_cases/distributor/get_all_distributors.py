from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import DistributorProps
from src.domain.protocols import UseCase


class GetAllDistributorsResult(TypedDict):
    distributors: list[DistributorProps]


class GetAllDistributors(UseCase[None, GetAllDistributorsResult]):
    @abstractmethod
    async def execute(self) -> GetAllDistributorsResult:
        pass
