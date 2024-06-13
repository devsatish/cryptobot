from exchanges import exchange
from typing import Self

class Coinbase(exchange.Exchange):
    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        # self.client = CoinbaseAccount(self.apiKey, self.apiSecret)
        self.name = self.__class__.__name__

    def get_client(self) -> Self:
        return self.client

    def get_symbol(self) -> str:
        return f"{self.currency}_to_{self.asset}"

    def symbol_ticker(self) -> None:
        try:
            response = self.client.exchange_rates([self.get_symbol()])
            self.process(response)
        except* Exception as e:
            # Handle multiple exceptions if needed

            for exc in e.exceptions:
                if isinstance(exc, ConnectionError):
                    print("Connection error occurred:", exc)
                elif isinstance(exc, TimeoutError):
                    print("Timeout error occurred:", exc)
                else:
                    print("An unexpected error occurred:", exc)