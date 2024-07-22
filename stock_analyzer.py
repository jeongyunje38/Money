import pandas as pd
import yfinance as yf
import talib


class StockAnalyzer:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_RSI(data:pd.Series, period:int=14) -> pd.Series:
        rsi = talib.RSI(data, period)
        return rsi

    @staticmethod
    def get_SMA(data:pd.Series, windows:list=[5, 10, 20, 50, 100, 200]) -> pd.Series:
        sma = pd.Series({window:talib.SMA(data, window) for window in windows})
        return sma

    @staticmethod
    def get_EMA(data:pd.Series, windows:list=[5, 10, 20, 50, 100, 200]) -> pd.Series:
        ema = pd.Series({window:talib.EMA(data, window) for window in windows})
        return ema

    @staticmethod
    def get_split_dates(ticker:str) -> pd.Series:
        split_dates = yf.Ticker(ticker).splits
        split_dates.index = pd.to_datetime(split_dates.index).strftime("%Y-%m-%d")
        return split_dates

    @staticmethod
    def adjust_for_stock_splits(data:pd.DataFrame, split_dates:pd.DataFrame) -> pd.DataFrame:
        prod = 1
        last_split_date = "1900-01-01"
        targets = ["open", "high", "low", "close"]
        for ratio in split_dates.values:
            prod *= ratio
        for split_date, ratio in split_dates.items():
            for target in targets:
                data.loc[(last_split_date <= data["date"]) & (data["date"] < split_date), target] /= prod
            prod /= ratio
            last_split_date = split_date
        return data
