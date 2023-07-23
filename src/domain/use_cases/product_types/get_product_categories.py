from abc import abstractmethod
from typing import TypedDict

from src.domain.protocols.use_case import UseCase


class GetProductCategoriesParams(TypedDict):
    product_type: str


class GetProductCategoriesResult(TypedDict):
    product_categories: list[str]


class GetProductCategories(
    UseCase[GetProductCategoriesParams, GetProductCategoriesResult]
):
    @abstractmethod
    async def execute(
        self, params: GetProductCategoriesParams
    ) -> GetProductCategoriesResult:
        pass
