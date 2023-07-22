from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import DistributorProps
from src.domain.protocols import UseCase


class EditDistributorParams(TypedDict):
    distributor: DistributorProps


class EditDistributorResult(TypedDict):
    crypted_id: str


class EditDistributor(UseCase[EditDistributorParams, EditDistributorResult]):
    @abstractmethod
    async def execute(self, params: EditDistributorParams) -> EditDistributorResult:
        pass
