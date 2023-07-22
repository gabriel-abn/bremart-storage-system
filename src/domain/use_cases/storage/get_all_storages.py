from abc import abstractmethod
from typing import TypedDict

from src.domain.entities.storage import StorageProps
from src.domain.protocols.use_case import UseCase


class GetAllStoragesResult(TypedDict):
    storages: list[StorageProps]


class GetAllStorages(UseCase[None, GetAllStoragesResult]):
    @abstractmethod
    async def execute(self) -> GetAllStoragesResult:
        pass
