from abc import abstractmethod
from typing import TypedDict

from src.domain.protocols.use_case import UseCase


class GetTypesAndCategoriesResult(TypedDict):
    types_list: list[dict[{"type": str, "categories": list[str]}]]


class GetTypesAndCategories(UseCase[None, GetTypesAndCategoriesResult]):
    @abstractmethod
    def execute(self) -> GetTypesAndCategoriesResult:
        pass
