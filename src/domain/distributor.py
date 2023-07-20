from typing import TypedDict

from src.domain.common import DomainError, Entity


class DistributorProps(TypedDict):
    cnpj: str
    razao_social: str
    branch: str


class Distributor(Entity[DistributorProps]):
    def __init__(self, props: DistributorProps, id: str):
        super().__init__(props, id)

    @staticmethod
    def create(props: DistributorProps, id: str):
        if len(props["cnpj"]) != 14:
            raise DomainError("Distributor", "CNPJ not valid.")

        return Distributor(props, id)
