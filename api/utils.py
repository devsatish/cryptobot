from datetime import datetime
from typing import TypeVar, Generic, Dict

T = TypeVar('T')
K = TypeVar('K')

def format_date(date: datetime) -> str:
    return date.strftime('%Y-%m-%d %H:%M')


def format_pair(currency: str | T, asset: str | T) -> str:
    if isinstance(currency, str) and isinstance(asset, str):
        return currency + '_' + asset
    else:
        return currency.symbol + '_' + asset.symbol


def filter_keys(data: Dict[K, T], keys: Dict[K, T]) -> Dict[K, T]:
    return {k: v for k, v in data.items() if k not in keys}