from abc import abstractmethod
from typing import TypedDict

from src.domain.protocols.use_case import UseCase


class RemoveStorageParams(TypedDict):
    storage_id: str


class RemoveStorageResult(TypedDict):
    removed: bool


class RemoveStorage(UseCase[RemoveStorageParams, RemoveStorageResult]):
    @abstractmethod
    def execute(self, params: RemoveStorageParams) -> RemoveStorageResult:
        pass
