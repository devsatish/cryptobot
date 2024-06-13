from datetime import datetime
from time import sleep
from typing import Self
from strategy import Strategy


class Debug(Strategy):
    def __init__(self, exchange, timeout=60, *args, **kwargs) -> None:
        super().__init__(exchange, timeout, *args, **kwargs)

    def run(self: Self) -> None:
        print(datetime.now().time())
        sleep(10)