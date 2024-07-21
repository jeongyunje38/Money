import os

from stock_analyzer import StockAnalyzer
from stock_fetcher import StockFetcher
from stock_predictor import StockPredictor
from visualizer import Visualizer

api_key = os.environ["ALPACA_API_KEY"]
secret_key = os.environ["ALPACA_SECRET_KEY"]
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2023-12-25"

fetcher = StockFetcher(api_key, secret_key)
raw_data = fetcher.get_data(ticker, start_date, end_date)
data = fetcher.format_data(raw_data)
dates = StockAnalyzer.get_split_dates(ticker)
data = StockAnalyzer.adjust_for_stock_splits(data, dates)
print(data)
