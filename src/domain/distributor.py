from typing import TypedDict

from common.domain_error import DomainError
from common.entity import Entity


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
            raise DomainError("CNPJ not valid.")

        return Distributor(props, id)
