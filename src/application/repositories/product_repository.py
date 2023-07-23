from abc import abstractmethod

from src.application.repositories.common.relational_repository import (
    RelationalRepository,
)
from src.domain.entities import Product, ProductProps


class IProductRepository(RelationalRepository):
    @abstractmethod
    async def register(self, product: Product) -> dict[{"id": str}]:
        pass

    @abstractmethod
    async def get_by_id(self, product_id: str) -> ProductProps:
        pass

    @abstractmethod
    async def get_by_barcode(self, barcode: str) -> ProductProps:
        pass

    @abstractmethod
    async def get_all(self) -> list[ProductProps]:
        pass
