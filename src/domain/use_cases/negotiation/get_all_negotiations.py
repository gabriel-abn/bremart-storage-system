from abc import abstractmethod
from typing import TypedDict

from src.domain.entities.negotiation import NegotiationProps
from src.domain.protocols.use_case import UseCase


class GetAllNegotiationsResult(TypedDict):
    negotiations: list[NegotiationProps]


class GetAllNegotiations(UseCase[None, GetAllNegotiationsResult]):
    @abstractmethod
    def execute(self) -> GetAllNegotiationsResult:
        pass
