from abc import abstractmethod
from typing import TypedDict

from src.domain.protocols.use_case import UseCase


class StockProductsParams(TypedDict):
    storage_id: int
    products: list[dict[{"id": int, "quantity": int}]]


class StockProductsResult(TypedDict):
    capacity_left: int


class StockProducts(UseCase[StockProductsParams, StockProductsResult]):
    @abstractmethod
    def execute(self, params: StockProductsParams) -> StockProductsResult:
        pass
