from abc import abstractmethod
from typing import TypedDict

from src.domain.protocols import UseCase


class CreateDistributorParams(TypedDict):
    cnpj: str
    razao_social: str
    branch: str


class CreateDistributorResult(TypedDict):
    crypted_id: str


class CreateDistributor(UseCase[CreateDistributorParams, CreateDistributorResult]):
    @abstractmethod
    def execute(self, params: CreateDistributorParams) -> CreateDistributorResult:
        pass
