from models.model import AbstractModel
from typing import Self

class Currency(AbstractModel):
    resource_name = 'currencies'

    name: str = ''
    symbol: str = ''
    fiat: bool

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def update_currency(self: Self, name: str, symbol: str, fiat: bool) -> None:
        self.name = name
        self.symbol = symbol
        self.fiat = fiat