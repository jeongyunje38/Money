import pandas as pd
import yfinance as yf


class StockAnalyzer:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_moving_averages(data:pd.DataFrame, windows:list) -> dict:
        ma = {window:data["close"].rolling(window).mean() for window in windows}
        return ma

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
