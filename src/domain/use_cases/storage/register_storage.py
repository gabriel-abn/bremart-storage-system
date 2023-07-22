from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import StorageProps
from src.domain.protocols import UseCase


class RegisterStorageParams(TypedDict):
    storage: StorageProps


class RegisterStorageResult(TypedDict):
    crypted_id: str


class RegisterStorage(UseCase[RegisterStorageParams, RegisterStorageResult]):
    @abstractmethod
    async def execute(self, params: RegisterStorageParams) -> RegisterStorageResult:
        pass
