import talib


class StockUtils:

    def __init__(self):
        pass

    @staticmethod
    def get_ATR(stock_data, period):

        high = stock_data.data["high"]
        low = stock_data.data["low"]
        close = stock_data.data["close"]

        return talib.ATR(high, low, close, period)

    @staticmethod
    def get_max_high(stock_data, period):

        return talib.MAX(stock_data.data["high"], timeperiod=period)
