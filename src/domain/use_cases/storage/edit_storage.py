from abc import abstractmethod
from typing import TypedDict

from src.domain.entities.storage import StorageProps
from src.domain.protocols.use_case import UseCase


class EditStorageParams(TypedDict):
    storage: StorageProps


class EditStorageResult(TypedDict):
    storage: StorageProps


class EditStorage(UseCase[EditStorageParams, EditStorageResult]):
    @abstractmethod
    async def execute(self, params: EditStorageParams) -> EditStorageResult:
        pass
