from abc import abstractmethod
from typing import TypedDict

from src.domain.entities import NegotiationProps
from src.domain.protocols import UseCase


class CreateNegotiationParams(TypedDict):
    negotiation: NegotiationProps


class CreateNegotiationResult(TypedDict):
    crypted_id: str


class CreateNegotiation(UseCase[CreateNegotiationParams, CreateNegotiationResult]):
    @abstractmethod
    async def execute(self, params: CreateNegotiationParams) -> CreateNegotiationResult:
        pass
