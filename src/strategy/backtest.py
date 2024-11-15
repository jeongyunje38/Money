import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.util.date_utils import DateUtils
from src.strategy.strategy import Strategy
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pandas import DataFrame
from src.util.enums import *


class Backtest:

    def __init__(self, init_balance: int):

        self._init_balance = init_balance

    @property
    def init_balance(self):

        return self._init_balance

    def run(
        self, stock_data: DataFrame, strategy: Strategy, fr: datetime, to: datetime
    ):

        if stock_data.data.iloc[-1]["date"] < to:

            print("Backtest: Required more data")

            return

        balance = self._init_balance
        position = 0
        queue = strategy.generate_signals(
            stock=stock_data,
            fr=fr,
            to=to,
        )

        while len(queue):

            curr_signal = queue.get_next()
            close_price = float(
                stock_data.data[stock_data.data["date"] == curr_signal.timing][
                    "close"
                ].squeeze()
            )
            change = curr_signal.quantity * close_price

            if curr_signal.action == TradingAction.BUY:

                if balance >= change:

                    balance -= change
                    position += curr_signal.quantity
                    print(f"{curr_signal.timing}: -{change}")

            elif curr_signal.action == TradingAction.SELL:

                if position >= curr_signal.quantity:

                    balance += change
                    position -= curr_signal.quantity
                    print(f"{curr_signal.timing}: +{change}")

        last_close_price = float(
            stock_data.data.loc[stock_data.data["date"] == to, "close"].squeeze()
        )
        balance += last_close_price * position
        print(balance)
