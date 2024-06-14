from datetime import datetime
from time import sleep
from strategy import Strategy
from typing import Self

class Debug(Strategy):
    def __init__(self, exchange: str, timeout: int = 60, *args, **kwargs) -> None:
        super().__init__(exchange, timeout, *args, **kwargs)

    def run(self) -> None:
        print(datetime.now().time())
        sleep(10)