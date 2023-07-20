from datetime import datetime
from typing import TypedDict

from src.domain.common import DomainError, Entity


class ShipmentProps(TypedDict):
    type: str
    source: str
    destiny: float
    start_date: datetime
    estimated_end_date: datetime
    cargos: list[dict[{"purchase": str, "products": list[str]}]]


class Shipment(Entity[ShipmentProps]):
    def __init__(self, props: ShipmentProps, id: str) -> None:
        super().__init__(props, id)

    @staticmethod
    def create(props: ShipmentProps, id: str):
        if props["type"] not in ["AIR", "SEA", "LAND"]:
            raise DomainError("Shipment", "Type is not valid")

        if props["source"] == props["destiny"]:
            raise DomainError("Shipment", "Source and destiny are the same")

        if props["cargos"] == []:
            raise DomainError("Shipment", "Cargos are empty")

        if (
            props["start_date"] > props["estimated_end_date"]
            or props["start_date"] == props["estimated_end_date"]
        ):
            raise DomainError(
                "Shipment",
                "Dates are not valid, start date must be before estimated end date",
            )

        return Shipment(props, id)
