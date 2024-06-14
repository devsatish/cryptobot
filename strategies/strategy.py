import threading
import time
from datetime import datetime
from abc import ABC, abstractmethod
from decouple import config
from typing import Self

from models.order import Order
from models.price import Price


class Strategy(ABC):
    TRADING_MODE_TEST = 'test'
    TRADING_MODE_REAL = 'real'

    price: Price

    def __init__(self, exchange, interval: int = 60, *args, **kwargs):
        self.exchange = exchange
        self._timer: threading.Timer | None = None
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.portfolio = {}
        self.test = bool(config('TRADING_MODE') != self.TRADING_MODE_REAL)

    def _run(self) -> None:
        self.is_running = False
        self.start()
        self.set_price(self.exchange.symbol_ticker())
        self.run()

    @abstractmethod
    def run(self) -> None:
        pass

    def start(self) -> None:
        if not self.is_running:
            print(datetime.now())
            if self._timer is None:
                self.next_call = time.time()
            else:
                self.next_call += self.interval

            self._timer = threading.Timer(self.next_call - time.time(), self._run)
            self._timer.start()
            self.is_running = True

    def stop(self) -> None:
        if self._timer:
            self._timer.cancel()
        self.is_running = False

    def get_portfolio(self) -> None:
        self.portfolio = {
            'currency': self.exchange.get_asset_balance(self.exchange.currency),
            'asset': self.exchange.get_asset_balance(self.exchange.asset)
        }

    def get_price(self) -> Price:
        return self.price

    def set_price(self, price: Price) -> None:
        self.price = price

    def buy(self, **kwargs) -> None:
        order = Order(
            currency=self.exchange.currency,
            asset=self.exchange.asset,
            symbol=self.exchange.get_symbol(),
            type=Order.TYPE_LIMIT,
            side=Order.BUY,
            test=self.test,
            **kwargs
        )
        self.order(order)

    def sell(self, **kwargs) -> None:
        order = Order(
            currency=self.exchange.currency,
            asset=self.exchange.asset,
            symbol=self.exchange.get_symbol(),
            side=Order.SELL,
            test=self.test,
            **kwargs
        )
        self.order(order)

    def order(self, order: Order) -> None:
        print(order)
        if self.test:
            exchange_order = self.exchange.test_order(order)
        else:
            exchange_order = self.exchange.order(order)

        print(exchange_order)