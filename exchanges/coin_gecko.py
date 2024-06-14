from pycoingecko import CoinGeckoAPI
from exchanges.exchange import Exchange

class CoinGecko(Exchange):
    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.name = self.__class__.__name__
        self.client = CoinGeckoAPI()

    def get_client(self) -> CoinGeckoAPI:
        return self.client

    def symbol_ticker(self) -> list:
        return self.client.get_coin_ticker_by_id(self.currency)['tickers']