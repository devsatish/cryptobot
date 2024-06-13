from pycoingecko import CoinGeckoAPI
from exchanges.exchange import Exchange
from typing import Self

class CoinGecko(Exchange):
    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.name = self.__class__.__name__
        self.client = CoinGeckoAPI()

    def get_client(self) -> Self:
        return self.client

    def symbol_ticker(self):
        return self.client.get_coin_ticker_by_id(self.currency)['tickers']

    def handle_exceptions(self):
        try:
            # Example operation that might raise multiple exceptions
            pass
        except* (ValueError, TypeError) as e:
            # Handle multiple exceptions using the new except* syntax
            print(f"An error occurred: {e}")