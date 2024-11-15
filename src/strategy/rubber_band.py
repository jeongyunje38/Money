import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from datetime import datetime

from src.util.date_utils import DateUtils
from src.util.enums import TradingAction, PriorityLevel
from src.util.stock_utils import StockUtils
from src.data.stock_data import StockData
from src.strategy.strategy import Strategy
from src.trading.trading_queue import TradingQueue
from trading.signal import Signal


class RubberBand(Strategy):

    def __init__(self):

        super().__init__()

    def generate_signals(self, stock: StockData, fr: datetime, to: datetime):

        queue = TradingQueue()

        period = 5
        coeff = 2.5

        atr = StockUtils.get_ATR(stock, period)
        max_high = StockUtils.get_max_high(stock, period)
        band = max_high - coeff * atr

        buy_timings = stock.data.loc[stock.data["close"] < band, "date"]
        # signal 생성 추가

        return queue
