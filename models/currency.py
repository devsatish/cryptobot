from models.model import AbstractModel
from typing import Self

class Currency(AbstractModel):
    resource_name = 'currencies'

    name: str = ''
    symbol: str = ''
    fiat: bool

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def update_currency(self, name: str, symbol: str, fiat: bool) -> Self:
        self.name = name
        self.symbol = symbol
        self.fiat = fiat
        return self

    def handle_exceptions(self) -> None:
        try:
            # Some code that might raise multiple exceptions
            pass
        except* (ValueError, TypeError) as e:
            # Handle multiple exceptions
            print(f"An error occurred: {e}")