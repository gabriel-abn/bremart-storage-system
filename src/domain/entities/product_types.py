from enum import Enum
from typing import Type, TypedDict


class ProductTypes(Enum):
    BOOK = "BOOK"
    CLOTHING = "CLOTHING"
    ELECTRONICS = "ELETRONICS"
    FURNITURE = "FURNITURE"
    HEALTH = "HEALTH"
    HOME = "HOME"


categories: list[tuple[ProductTypes, list[str]]] = [
    (ProductTypes.BOOK, ["For Kids", "Fiction", "Non-Fiction"]),
    (ProductTypes.CLOTHING, ["Men", "Women", "Kids"]),
    (ProductTypes.ELECTRONICS, ["Mobile", "Laptop", "Desktop"]),
    (ProductTypes.FURNITURE, ["Bedroom", "Living Room", "Kitchen"]),
    (ProductTypes.HEALTH, ["Vitamins", "Supplements", "Medicines"]),
    (ProductTypes.HOME, ["Kitchen", "Bathroom", "Bedroom"]),
]
