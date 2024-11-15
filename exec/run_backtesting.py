import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from datetime import datetime

from src.strategy.backtest import Backtest
from src.strategy.russell_rebalancing import RussellRebalancing
from src.strategy.rubber_band import RubberBand
from src.data.stock_data_manager import StockDataManager


sdm = StockDataManager(
    db_user=os.environ["MYSQL_USER"],
    db_password=os.environ["MYSQL_PASSWORD"],
    db_host="localhost",
    db_port="3306",
    db_name="STOCK",
    alpaca_api_key=os.environ["ALPACA_API_KEY"],
    alpaca_secret_key=os.environ["ALPACA_SECRET_KEY"],
)

ticker = "AAPL"
balance = 100000
fr = datetime(2020, 1, 1)
to = datetime(2024, 10, 1)

data = sdm.load_from_db(ticker=ticker)
bt = Backtest(init_balance=balance)
# bt.run(stock_data=data, strategy=RussellRebalancing(), fr=fr, to=to)
bt.run(stock_data=data, strategy=RubberBand(), fr=fr, to=to)
