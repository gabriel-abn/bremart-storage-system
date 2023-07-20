from typing import TypedDict

from src.domain.common import DomainError, Entity


class StorageProps(TypedDict):
    local: dict[
        {
            "country": str,
            "state": str,
            "city": str,
            "address": str,
            "cep": str,
        }
    ]
    capacity: int
    items: list[
        dict[
            {
                "product_id": str,
                "quantity": int,
            }
        ]
    ]


class Storage(Entity[StorageProps]):
    def __init__(self, props: StorageProps, id: str) -> None:
        super().__init__(props, id)

    @staticmethod
    def create(props: StorageProps, id: str):
        if props["capacity"] <= 0:
            raise DomainError("Storage", "Storage capacity must be greater than 0")

        return Storage(props, id)
