import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from tqdm import tqdm

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

tickers = [
    "AAPL",
    "NVDA",
    "MSFT",
    "GOOGL",
    "AMZN",
    "META",
    # "BRK-A",
    "TSM",
    "AVGO",
    "LLY",
    "TSLA",
]
start_date = "2020-01-01"
end_date = "2024-10-20"

for ticker in tqdm(tickers):

    data = sdm.get_data_from_alpaca(
        ticker=ticker, start_date=start_date, end_date=end_date
    )
    data = sdm.format_data(data)
    sdm.save_to_db(data)
