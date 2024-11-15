import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

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
data = sdm.load_from_db(ticker=ticker)
print(data)
