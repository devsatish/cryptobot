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

    def set_currency(self: Self, symbol: str) -> None:
        self.currency = symbol

    def set_asset(self: Self, symbol: str) -> None:
        self.asset = symbol

    def set_strategy(self: Self, strategy: Strategy) -> None:
        self.strategy = strategy

    def compute_symbol_pair(self: Self) -> str:
        return utils.format_pair(self.currency, self.asset)

    # abstract methods

    # Override to set current exchange symbol pair notation (default with _ separator currency_asset ex: eur_btc)
    @abstractmethod
    def get_symbol(self: Self) -> str:
        return self.compute_symbol_pair()

    # Get current symbol ticker
    @abstractmethod
    def symbol_ticker(self: Self) -> None:
        pass

    # Get current symbol ticker candle for given interval
    @abstractmethod
    def symbol_ticker_candle(self: Self, interval: int) -> None:
        pass

    # Get current symbol historic value
    @abstractmethod
    def historical_symbol_ticker_candle(self: Self, start: datetime.datetime, end: datetime.datetime = None, interval: int = 60) -> None:
        pass

    # Get balance for a given currency
    @abstractmethod
    def get_asset_balance(self: Self, currency: str) -> None:
        pass

    # Create an exchange order
    @abstractmethod
    def order(self: Self, order: Order) -> None:
        pass

    # Create an exchange test order
    @abstractmethod
    def test_order(self: Self, order: Order) -> None:
        pass

    # Check an exchange order status
    @abstractmethod
    def check_order(self: Self, orderId: str) -> None:
        pass

    # Cancel an exchange order
    @abstractmethod
    def cancel_order(self: Self, orderId: str) -> None:
        pass

    # WebSocket related methods

    @abstractmethod
    def get_socket_manager(self: Self, purchase: bool) -> None:
        pass

    @abstractmethod
    def websocket_event_handler(self: Self, msg: dict) -> None:
        pass

    def start_socket(self: Self) -> None:
        print('Starting WebSocket connection...')
        self.socketManager.start()

    def close_socket(self: Self) -> None:
        self.socketManager.stop_socket(self.socket)
        self.socketManager.close()
        # properly terminate WebSocket
        reactor.stop()

    @abstractmethod
    def start_symbol_ticker_socket(self: Self, symbol: str) -> None:
        pass