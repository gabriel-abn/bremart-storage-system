from enum import Enum
from typing import NotRequired, TypedDict

from domain.common import Entity


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
        return Negotiation({"status": NegotiationStatus.PENDING, **props}, id)
