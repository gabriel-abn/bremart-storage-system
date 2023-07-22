from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import DistributorProps
from src.domain.protocols import UseCase


class CreateDistributorParams(TypedDict):
    distributor: DistributorProps


class CreateDistributorResult(TypedDict):
    crypted_id: str


class CreateDistributor(UseCase[CreateDistributorParams, CreateDistributorResult]):
    @abstractmethod
    async def execute(self, params: CreateDistributorParams) -> CreateDistributorResult:
        pass
