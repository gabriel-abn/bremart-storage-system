from enum import Enum
from typing import NotRequired, TypedDict

from src.domain.protocols import DomainError, Entity


class NegotiationStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class NegotiationProps(TypedDict):
    distributor_id: str
    total_value: float
    products: list[
        dict[
            {
                "product_id": str,
                "quantity": int,
            }
        ]
    ]
    status: NotRequired[NegotiationStatus]


class Negotiation(Entity[NegotiationProps]):
    def __init__(self, props: NegotiationProps, id: str) -> None:
        super().__init__(props, id)

    @staticmethod
    def create(props: NegotiationProps, id: str):
        if props["products"] == []:
            raise DomainError("Negotiation", "Products list cannot be empty.")

        if props["total_value"] <= 0:
            raise DomainError("Negotiation", "Invalid negotiation total value.")

        return Negotiation({"status": NegotiationStatus.PENDING, **props}, id)
