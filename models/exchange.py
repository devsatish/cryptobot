from datetime import datetime
from api import utils
from models.model import AbstractModel
from typing import Self

class Exchange(AbstractModel):
    resource_name: str = 'exchanges'

    id: str = ''
    name: str = ''

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def update_name(self: Self, new_name: str) -> None:
        self.name = new_name

    def get_id(self: Self) -> str:
        return self.id

    def set_id(self: Self, new_id: str) -> None:
        self.id = new_id