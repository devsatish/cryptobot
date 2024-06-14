import datetime
from api import utils
from abc import ABC, abstractmethod
from twisted.internet import reactor
from strategies.strategy import Strategy
from models.order import Order
from typing import Self


class Exchange(ABC):
    currency: str
    asset: str
    strategy: Strategy

    def __init__(self, key: str, secret: str):
        self.apiKey = key
        self.apiSecret = secret
        self.name = None
        self.client = None
        self.socketManager = None
        self.socket = None
        self.currency = ''
        self.asset = ''
        self.strategy = None

    def set_currency(self, symbol: str) -> None:
        self.currency = symbol

    def set_asset(self, symbol: str) -> None:
        self.asset = symbol

    def set_strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def compute_symbol_pair(self) -> str:
        return utils.format_pair(self.currency, self.asset)

    # abstract methods

    # Override to set current exchange symbol pair notation (default with _ separator currency_asset ex: eur_btc)
    @abstractmethod
    def get_symbol(self) -> str:
        return self.compute_symbol_pair()

    # Get current symbol ticker
    @abstractmethod
    def symbol_ticker(self) -> dict:
        pass

    # Get current symbol ticker candle for given interval
    @abstractmethod
    def symbol_ticker_candle(self, interval: int) -> dict:
        pass

    # Get current symbol historic value
    @abstractmethod
    def historical_symbol_ticker_candle(self, start: datetime.datetime, end: datetime.datetime = None, interval: int = 60) -> list:
        pass

    # Get balance for a given currency
    @abstractmethod
    def get_asset_balance(self, currency: str) -> float:
        pass

    # Create an exchange order
    @abstractmethod
    def order(self, order: Order) -> dict:
        pass

    # Create an exchange test order
    @abstractmethod
    def test_order(self, order: Order) -> dict:
        pass

    # Check an exchange order status
    @abstractmethod
    def check_order(self, orderId: str) -> dict:
        pass

    # Cancel an exchange order
    @abstractmethod
    def cancel_order(self, orderId: str) -> dict:
        pass

    # WebSocket related methods

    @abstractmethod
    def get_socket_manager(self, purchase: bool) -> None:
        pass

    @abstractmethod
    def websocket_event_handler(self, msg: dict) -> None:
        pass

    def start_socket(self) -> None:
        print('Starting WebSocket connection...')
        self.socketManager.start()

    def close_socket(self) -> None:
        self.socketManager.stop_socket(self.socket)
        self.socketManager.close()
        # properly terminate WebSocket
        reactor.stop()

    @abstractmethod
    def start_symbol_ticker_socket(self, symbol: str) -> None:
        pass