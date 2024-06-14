from api.rest import Rest
from typing import Self

class AbstractModel(Rest):
    resource_name: str = ''

    def __init__(self, **kwargs: dict[str, any]) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)