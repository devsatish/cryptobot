from exchanges.exchange import Exchange
from strategies.strategy import Strategy
from typing import Self


class Logger(Strategy):
    def __init__(self, exchange: Exchange, timeout: int = 60, *args, **kwargs) -> None:
        super().__init__(exchange, timeout, *args, **kwargs)

    def run(self) -> None:
        print('*******************************')
        print('Exchange: ', self.exchange.name)
        print('Pair: ', self.exchange.get_symbol())
        print('Price: ', self.price.current)