from abc import ABC
from datetime import datetime
from typing import Generic, TypeVar
from uuid import UUID

T = TypeVar("T")


class Entity(ABC, Generic[T]):
    __props: T
    __id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, props: T, id: str) -> None:
        self.__props = props
        self.__id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_update_dates(
        self,
    ) -> dict[{"created_at": datetime, "updated_at": datetime}]:
        return {"created_at": self.created_at, "updated_at": self.updated_at}

    def get_props(self) -> T:
        return self.__props

    def get_id(self) -> str:
        return self.__id
