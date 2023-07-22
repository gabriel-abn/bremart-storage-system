from abc import abstractmethod
from typing import TypedDict

from src.domain.entities.storage import StorageProps
from src.domain.protocols.use_case import UseCase


class GetStorageByIdParams(TypedDict):
    id: str


class GetStorageByIdResult(TypedDict):
    storage: StorageProps


class GetStorageById(UseCase[GetStorageByIdParams, GetStorageByIdResult]):
    @abstractmethod
    async def execute(self, params: GetStorageByIdParams) -> GetStorageByIdResult:
        pass
