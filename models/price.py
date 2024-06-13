from api import utils
from models.model import AbstractModel
from models.currency import Currency
from models.dataset import Dataset
from models.exchange import Exchange
from typing import Self


class Price(AbstractModel):
    resource_name = 'prices'

    dataset: str = ''
    pair: str = ''
    exchange: str = ''
    current: float = 0
    lowest: float = 0
    highest: float = 0
    volume: float = 0
    currency: str = ''
    asset: str = ''
    dataset: str = ''
    openAt: str

    relations = {'exchange': Exchange, 'currency': Currency, 'asset': Currency, 'dataset': Dataset}

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.pair = self.get_pair()

    def get_pair(self) -> str:
        return utils.format_pair(self.currency, self.asset)

    def some_method(self) -> Self:
        # Example method to demonstrate the use of Self type hint
        return self

    def handle_exceptions(self) -> None:
        try:
            # Some code that might raise multiple exceptions
            pass
        except* (ValueError, TypeError) as e:
            # Handle multiple exceptions using the new except* syntax
            for exc in e.exceptions:
                print(f"Handled exception: {exc}")