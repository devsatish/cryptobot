from datetime import datetime

from api import utils
from exchanges.exchange import Exchange
from models.dataset import Dataset
from strategies.strategy import Strategy
from typing import Self, TypeVar, Generic

T = TypeVar('T')

class Runner(Strategy, Generic[T]):
    def __init__(self: Self, exchange: Exchange, timeout=60, *args, **kwargs):
        super().__init__(exchange, timeout, *args, **kwargs)
        self.buy_price = 0
        self.sell_price = 0
        self.stop_loss = 0

        self.market_delta = 0

        self.advised = False
        self.waiting_order = False
        self.fulfilled_orders = []
        self.last_price = 0
        # create a dataset for the session
        self.dataset = Dataset().create(
            data={'exchange': self.exchange.name.lower(), 'periodStart': datetime.now(), 'candleSize': 60,
                  'currency': self.exchange.currency, 'asset': self.exchange.asset})

    def run(self: Self):
        print('*******************************')
        print('Exchange: ', self.exchange.name)
        print('Pair: ', self.exchange.get_symbol())
        print('Available: ', self.exchange.get_asset_balance(self.exchange.currency) + ' ' + self.exchange.currency)
        print('Available: ', self.exchange.get_asset_balance(self.exchange.currency) + ' ' + self.exchange.asset)
        print('Price: ', self.price.current)

        # Persist price
        print(self.dataset)
        print(self.price)
        response = self.price.create(data={"dataset": self.dataset.uuid})
        print(response)

    def handle_exceptions(self: Self):
        try:

            # Simulate some operations that might raise multiple exceptions
            result = self.exchange.perform_trade(self.buy_price, self.sell_price)
            if not result:
                raise ValueError("Trade could not be performed")
            self.fulfilled_orders.append(result)
        except* (ValueError, TypeError) as e:
            print(f"An error occurred: {e}")
            pass
        except* (ValueError, TypeError) as e:
            print(f"An error occurred: {e}")