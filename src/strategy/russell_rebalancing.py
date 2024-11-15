import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from datetime import datetime

from src.util.date_utils import DateUtils
from src.util.enums import TradingAction, PriorityLevel
from src.data.stock_data import StockData
from src.strategy.strategy import Strategy
from src.trading.trading_queue import TradingQueue
from trading.signal import Signal


class RussellRebalancing(Strategy):

    def __init__(self):

        super().__init__()

    def generate_signals(self, stock_data: StockData, fr: datetime, to: datetime):

        queue = TradingQueue()

        quantity = 1.0
        strength = 1.0
        buy_month = 6
        buy_day = 23
        sell_month = 6
        sell_day = 30

        first_buy_timing = DateUtils.right_after_bd(
            dates=DateUtils.US_bd(fr=fr, to=to),
            ref=datetime(year=fr.year, month=buy_month, day=buy_day),
        )

        last_sell_timing = DateUtils.right_after_bd(
            dates=DateUtils.US_bd(fr=fr, to=to),
            ref=datetime(year=to.year, month=sell_month, day=sell_day),
        )

        fr_year = fr.year if fr <= first_buy_timing else fr.year + 1
        to_year = to.year if to >= last_sell_timing else to.year - 1

        for year in range(fr_year, to_year + 1):

            queue.add_signal(
                signal=Signal(
                    ticker=stock_data.ticker,
                    quantity=quantity,
                    action=TradingAction.BUY,
                    strength=strength,
                    timing=DateUtils.right_after_bd(
                        dates=DateUtils.US_bd(fr=fr, to=to),
                        ref=datetime(year=year, month=buy_month, day=buy_day),
                    ),
                    timestamp=datetime.now(),
                ),
                priority=PriorityLevel.MEDIUM,
            )

            queue.add_signal(
                signal=Signal(
                    ticker=stock_data.ticker,
                    quantity=quantity,
                    action=TradingAction.SELL,
                    strength=strength,
                    timing=DateUtils.right_after_bd(
                        dates=DateUtils.US_bd(fr=fr, to=to),
                        ref=datetime(year=year, month=sell_month, day=sell_day),
                    ),
                    timestamp=datetime.now(),
                ),
                priority=PriorityLevel.MEDIUM,
            )

        return queue
