from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import ProductProps
from src.domain.protocols import UseCase


class RegisterProductParams(TypedDict):
    product: ProductProps


class RegisterProductResult(TypedDict):
    crypted_id: str


class RegisterProduct(UseCase[RegisterProductParams, RegisterProductResult]):
    @abstractmethod
    async def execute(self, params: RegisterProductParams) -> RegisterProductResult:
        pass
