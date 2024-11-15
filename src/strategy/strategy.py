import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.data.stock_data import StockData
from datetime import datetime


class Strategy:

    def __init__(self):
        pass

    def generate_signals(self, stock_data: StockData, fr: datetime, to: datetime):
        raise NotImplementedError()
