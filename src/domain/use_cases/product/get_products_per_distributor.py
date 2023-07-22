from abc import abstractmethod
from typing import TypedDict

from src.domain.entities.product import ProductProps
from src.domain.protocols.use_case import UseCase


class GetProductsPerDistributorParams(TypedDict):
    cnpj: str


class GetProductsPerDistributorResult(TypedDict):
    products: list[ProductProps]


class GetProductsPerDistributor(
    UseCase[GetProductsPerDistributorParams, GetProductsPerDistributorResult]
):
    @abstractmethod
    async def execute(
        self, params: GetProductsPerDistributorParams
    ) -> GetProductsPerDistributorResult:
        pass
