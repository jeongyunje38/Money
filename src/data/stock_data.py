import pandas as pd
from sqlalchemy import Engine


class StockData:

    def __init__(self, ticker: str, data: pd.DataFrame):
        self._ticker: str = ticker
        self._data: pd.DataFrame = data

    def __str__(self):

        return f"ticker:{self.ticker}\ndata:\n{self.data}"

    @property
    def ticker(self) -> str:
        return self._ticker

    @property
    def data(self) -> pd.DataFrame:
        return self._data
