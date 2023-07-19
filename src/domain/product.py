from typing import TypedDict

from common.domain_error import DomainError
from common.entity import Entity


class ProductProps(TypedDict):
    name: str
    price: float
    description: str
    bar_code: str


class Product(Entity[ProductProps]):
    def __init__(self, props: ProductProps, id: str) -> None:
        super().__init__(props, id)

    @staticmethod
    def create(props: ProductProps, id: str):
        if props["name"] == "":
            raise DomainError("Name is required")

        if props["price"] == 0:
            raise DomainError("Price is required")

        return Product(props, id)
