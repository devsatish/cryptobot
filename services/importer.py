import sys
from datetime import datetime
from models.dataset import Dataset
from typing import Self


class Importer:
    def __init__(self, exchange, period_start: datetime, period_end: datetime | None = None, interval: int = 60, *args, **kwargs):
        self.exchange = exchange
        self.interval = interval
        self.period_start = period_start
        self.period_end = period_end
        self.launchedAt = datetime.now()
        self.dataset = Dataset().create(
            data={'exchange': '/api/exchanges/' + self.exchange.name.lower(), 'periodStart': self.period_start, 'periodEnd': self.period_end,
                  'candleSize': 60,
                  'currency': '/api/currencies/' + self.exchange.currency.lower(), 'asset': '/api/currencies/' + self.exchange.asset.lower()})

    def process(self: Self) -> None:
        try:
            for price in self.exchange.historical_symbol_ticker_candle(self.period_start, self.period_end, self.interval):
                print(price.create({'dataset': '/api/datasets/' + self.dataset.uuid}))

            execution_time = datetime.now() - self.launchedAt
            print('Execution time: ' + str(execution_time.total_seconds()) + ' seconds')
        except* (Exception,) as e:
            print(f"An error occurred: {e}")
        finally:
            sys.exit(0)