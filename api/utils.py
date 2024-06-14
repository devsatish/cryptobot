from datetime import datetime
from typing import Union, Dict, Any


def format_date(date: datetime) -> str:
    return date.strftime('%Y-%m-%d %H:%M')


def format_pair(currency: Union[str, Any], asset: Union[str, Any]) -> str:
    if isinstance(currency, str) and isinstance(asset, str):
        return currency + '_' + asset
    else:
        return currency.symbol + '_' + asset.symbol


def filter_keys(data: Dict[str, Any], keys: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if k not in keys}