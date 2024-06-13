from strategies.strategy import Strategy
from typing import Self, TypeVar, Generic

T = TypeVar('T')

class Arbitrage(Strategy, Generic[T]):
    def __init__(self, exchange, timeout: int = 60, *args, **kwargs) -> None:
        super().__init__(exchange, timeout, *args, **kwargs)
        self.exchanges = ['binance', 'bitfinex', 'kraken']
        self.currencies = ['bitcoin', 'ethereum', 'monero']
        self.asset = ['EUR']

    def run(self: Self) -> None:
        for coin in self.currencies:
            try:
                response = self.exchange.get_client().symbol_ticker()
                print(response)
            except* Exception as e:
                print(f"An error occurred: {e}")