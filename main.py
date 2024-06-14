#!/usr/bin/python3

import importlib
import signal
import sys
import threading
from decouple import config

from services.backtest import Backtest
from services.importer import Importer

exchange_name: str = config('EXCHANGE')
available_exchanges: list[str] = config('AVAILABLE_EXCHANGES').split(',')
mode: str = config('MODE')
strategy: str = config('STRATEGY')
trading_mode: str = config('TRADING_MODE')
interval: int = int(config('CANDLE_INTERVAL'))
currency: str = config('CURRENCY')
asset: str = config('ASSET')

if trading_mode == 'real':
    print("*** Caution: Real trading mode activated ***")
else:
    print("Test mode")

# Parse symbol pair from first command argument
if len(sys.argv) > 1:
    currencies = sys.argv[1].split('_')
    if len(currencies) > 1:
        currency = currencies[0]
        asset = currencies[1]

# Load exchange
print(f"Connecting to {exchange_name.capitalize()} exchange...")
exchangeModule = importlib.import_module(f'exchanges.{exchange_name}', package=None)
exchangeClass = getattr(exchangeModule, exchange_name.capitalize())
exchange = exchangeClass(config(f'{exchange_name.upper()}_API_KEY'), config(f'{exchange_name.upper()}_API_SECRET'))

# Load currencies
exchange.set_currency(currency)
exchange.set_asset(asset)

# Load strategy
strategyModule = importlib.import_module(f'strategies.{strategy}', package=None)
strategyClass = getattr(strategyModule, strategy.capitalize())
exchange.set_strategy(strategyClass(exchange, interval))

# mode
print(f"{mode} mode on {exchange.get_symbol()} symbol")
if mode == 'trade':
    exchange.strategy.start()

elif mode == 'live':
    exchange.start_symbol_ticker_socket(exchange.get_symbol())

elif mode == 'backtest':
    period_start: str = config('PERIOD_START')
    period_end: str = config('PERIOD_END')

    print(
        f"Backtest period from {period_start} to {period_end} with {interval} seconds candlesticks."
    )
    Backtest(exchange, period_start, period_end, interval)

elif mode == 'import':
    period_start: str = config('PERIOD_START')
    period_end: str = config('PERIOD_END')

    print(
        f"Import mode on {exchange.get_symbol()} symbol for period from {period_start} to {period_end} with {interval} seconds candlesticks."
    )
    importer = Importer(exchange, period_start, period_end, interval)
    importer.process()

else:
    print('Not supported mode.')


def signal_handler(signal: int, frame) -> None:
    if exchange.socket:
        print('Closing WebSocket connection...')
        exchange.close_socket()
        sys.exit(0)
    else:
        print('stopping strategy...')
        exchange.strategy.stop()
        sys.exit(0)


# Listen for keyboard interrupt event
signal.signal(signal.SIGINT, signal_handler)
forever = threading.Event()
forever.wait()
exchange.strategy.stop()
sys.exit(0)