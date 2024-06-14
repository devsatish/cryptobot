from strategies.strategy import Strategy
from typing import List

class Arbitrage(Strategy):
    def __init__(self, exchange, timeout: int = 60, *args, **kwargs):
        super().__init__(exchange, timeout, *args, **kwargs)
        self.exchanges: List[str] = ['binance', 'bitfinex', 'kraken']
        self.currencies: List[str] = ['bitcoin', 'ethereum', 'monero']
        self.asset: List[str] = ['EUR']

    def run(self) -> None:
        for coin in self.currencies:
            response = self.exchange.get_client().symbol_ticker()
            print(response)