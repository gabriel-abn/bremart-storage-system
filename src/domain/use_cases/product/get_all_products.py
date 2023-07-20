from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import ProductProps
from src.domain.protocols import UseCase


class GetAllProductsResult(TypedDict):
    products: list[ProductProps]


class GetAllProducts(UseCase[None, GetAllProductsResult]):
    @abstractmethod
    def execute(self) -> GetAllProductsResult:
        pass
