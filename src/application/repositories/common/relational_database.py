from abc import ABC, abstractmethod


class RelationalDatabase(ABC):
    @abstractmethod
    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        database: str,
        connection: object = None,
        cursor: object = None,
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = connection
        self.cursor = cursor

    @abstractmethod
    async def connect(self, app_name: str) -> bool:
        pass

    @abstractmethod
    async def query(
        self,
        query: str,
        query_params: dict,
    ) -> dict:
        pass

    @abstractmethod
    async def queryNoCommit(
        self,
        query: str,
        query_params: dict,
    ) -> dict:
        pass

    @abstractmethod
    async def commit(self) -> bool:
        pass

    @abstractmethod
    async def close(self) -> bool:
        pass
