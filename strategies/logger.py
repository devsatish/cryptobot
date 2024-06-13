from exchanges.exchange import Exchange
from strategies.strategy import Strategy
from typing import Self


class Logger(Strategy):
    def __init__(self, exchange: Exchange, timeout=60, *args, **kwargs):
        super().__init__(exchange, timeout, *args, **kwargs)

    def run(self: Self) -> None:
        print('*******************************')
        print('Exchange: ', self.exchange.name)
        print('Pair: ', self.exchange.get_symbol())
        print('Price: ', self.price.current)

    def handle_exceptions(self: Self) -> None:
        try:
            self.run()
        except* (ValueError, TypeError) as e:
            print(f"An error occurred: {e}")