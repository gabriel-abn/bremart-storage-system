from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import ProductProps
from src.domain.protocols import UseCase


class EditProductParams(TypedDict):
    product: ProductProps


class EditProductResult(TypedDict):
    product: ProductProps


class EditProduct(UseCase[EditProductParams, EditProductResult]):
    @abstractmethod
    async def execute(self, params: EditProductParams) -> EditProductResult:
        pass
