from abc import abstractmethod
from typing import TypedDict

from src.domain.protocols import UseCase


class GetProductTypesResult(TypedDict):
    product_types: list[str]


class GetProductTypes(UseCase[None, GetProductTypesResult]):
    @abstractmethod
    def execute(self) -> GetProductTypesResult:
        pass
