from datetime import datetime
from typing import Self

from api import utils
from models.model import AbstractModel
from models.exchange import Exchange
from models.currency import Currency


class Dataset(AbstractModel):
    resource_name = 'datasets'

    pair: str = ''
    exchange: str = ''
    period_start: str = ''
    period_end: str = ''
    currency: str = ''
    asset: str = ''

    relations = {'exchange': Exchange, 'currency': Currency, 'asset': Currency}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pair = self.get_pair()

    def get_pair(self) -> str:
        return utils.format_pair(self.currency, self.asset)

    def update_dataset(self) -> Self:
        # Example method to demonstrate the use of `Self` type hint

        self.pair = self.get_pair()
        self.period_start = datetime.now().isoformat()
        self.period_end = datetime.now().isoformat()
        # Assuming update logic involves refreshing the exchange and currency relations

            # Simulate code that might raise multiple exceptions
            value = int("not_a_number")  # This will raise a ValueError
            result = 10 / 0  # This will raise a ZeroDivisionError
        self.currency = Currency.get_latest()
        self.asset = Currency.get_latest()
        return self

    def handle_exceptions(self):
        try:

            # Simulate code that might raise multiple exceptions
            value = int("not_a_number")  # This will raise a ValueError
            result = 10 / 0  # This will raise a ZeroDivisionError
            pass
        except* (ValueError, TypeError) as e:
            # Handle multiple exceptions using the new `except*` syntax
            for exc in e.exceptions:
                print(f"Handled exception: {exc}")