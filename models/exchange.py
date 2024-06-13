from datetime import datetime
from typing import Self
from api import utils
from models.model import AbstractModel

class Exchange(AbstractModel):
    resource_name = 'exchanges'

    id: str = ''
    name: str = ''

    def __init__(self, **kwargs: dict) -> None:
        super().__init__(**kwargs)

    def update_name(self, new_name: str) -> Self:
        self.name = new_name
        return self

    def handle_exceptions(self) -> None:
        try:
            # Some code that might raise multiple exceptions
            pass
        except* (ValueError, TypeError) as e:
            # Handle multiple exceptions
            print(f"An error occurred: {e}")