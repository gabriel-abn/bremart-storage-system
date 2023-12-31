from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import DistributorProps
from src.domain.protocols import UseCase


class GetDistributorParams(TypedDict):
    cnpj: str


class GetDistributorResult(TypedDict):
    distributor: DistributorProps


class GetDistributor(UseCase[GetDistributorParams, GetDistributorResult]):
    @abstractmethod
    async def execute(self, params: GetDistributorParams) -> GetDistributorResult:
        pass
