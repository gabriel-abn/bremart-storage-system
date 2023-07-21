from abc import abstractmethod
from typing import TypedDict

from src.domain.entities.negotiation import NegotiationProps
from src.domain.protocols.use_case import UseCase


class GetNegotiationParams(TypedDict):
    negotiation_id: str


class GetNegotiationResult(TypedDict):
    negotiation: NegotiationProps


class GetNegotiation(UseCase[GetNegotiationParams, GetNegotiationResult]):
    @abstractmethod
    def execute(self, params: GetNegotiationParams) -> GetNegotiationResult:
        pass
