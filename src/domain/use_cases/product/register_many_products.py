from abc import abstractmethod
from typing import TypedDict

from src.domain.entities.product import ProductProps
from src.domain.protocols.use_case import UseCase


class RegisterManyProductsParams(TypedDict):
    products: list[ProductProps]


class RegisterManyProductsResult(TypedDict):
    products_id: list[str]


class RegisterManyProducts(
    UseCase[RegisterManyProductsParams, RegisterManyProductsResult]
):
    @abstractmethod
    async def execute(
        self, params: RegisterManyProductsParams
    ) -> RegisterManyProductsResult:
        pass
