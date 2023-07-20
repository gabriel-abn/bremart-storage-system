from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import ProductProps
from src.domain.protocols import UseCase


class GetProductParams(TypedDict):
    bar_code: str


class GetProductResult(TypedDict):
    product: ProductProps


class GetProduct(UseCase[GetProductParams, GetProductResult]):
    @abstractmethod
    def execute(self, params: GetProductParams) -> GetProductResult:
        pass
