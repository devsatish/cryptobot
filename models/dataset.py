from datetime import datetime
from api import utils
from models.model import AbstractModel
from models.exchange import Exchange
from models.currency import Currency
from typing import Self

class Dataset(AbstractModel):
    resource_name = 'datasets'

    pair: str = ''
    exchange: str = ''
    period_start: str = ''
    period_end: str = ''
    currency: str = ''
    asset: str = ''

    relations = {'exchange': Exchange, 'currency': Currency, 'asset': Currency}

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.pair = self.get_pair()

    def get_pair(self) -> str:
        return utils.format_pair(self.currency, self.asset)

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        instance = cls(**data)
        return instance

    def to_dict(self) -> dict:
        return {
            'pair': self.pair,
            'exchange': self.exchange,
            'period_start': self.period_start,
            'period_end': self.period_end,
            'currency': self.currency,
            'asset': self.asset
        }