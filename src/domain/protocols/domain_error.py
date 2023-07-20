class DomainError(Exception):
    def __init__(self, name: str, message: str) -> None:
        self.args = (name, message)
        self.message = message
        self.__class__.__qualname__ = name
        self.__class__.__name__ = name

    def __str__(self) -> str:
        return self.message
