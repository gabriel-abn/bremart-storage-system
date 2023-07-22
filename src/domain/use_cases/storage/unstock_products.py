from abc import abstractmethod
from typing import TypedDict

from src.domain.protocols.use_case import UseCase


class UnstockProductsParams(TypedDict):
    storage_id: str
    products: list[dict[{"product_id": str, "quantity": int}]]


class UnstockProductsResult(TypedDict):
    capacity_left: int


class UnstockProducts(UseCase[UnstockProductsParams, UnstockProductsResult]):
    @abstractmethod
    async def execute(self, params: UnstockProductsParams) -> UnstockProductsResult:
        pass
