class ApplicationError(Exception):
    def __init__(self, message: str, class_name: str):
        self.message = message
        self.__class__.__name__ = class_name
        self.__class__.__qualname__ = class_name

    def __str__(self):
        return self.message
