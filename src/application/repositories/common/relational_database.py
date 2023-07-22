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
    def connect(self, app_name: str) -> bool:
        pass

    @abstractmethod
    def query(
        self,
        query: str,
        query_params: dict,
    ) -> dict:
        pass

    @abstractmethod
    def queryNoCommit(
        self,
        query: str,
        query_params: dict,
    ) -> dict:
        pass

    @abstractmethod
    def commit(self) -> bool:
        pass

    @abstractmethod
    def close(self) -> bool:
        pass
