import os

from src.tmp.stock_analyzer import StockAnalyzer
from stock_fetcher import StockFetcher
from stock_predictor import StockPredictor
from src.tmp.visualizer import Visualizer

api_key = os.environ["ALPACA_API_KEY"]
secret_key = os.environ["ALPACA_SECRET_KEY"]
ticker = "NVDA"
start_date = "2010-01-01"
end_date = "2020-01-01"

fetcher = StockFetcher(api_key, secret_key)
raw_data = fetcher.get_data(ticker, start_date, end_date)
data = fetcher.format_data(raw_data)
dates = StockAnalyzer.get_split_dates(ticker, start_date, end_date)
data = StockAnalyzer.adjust_for_stock_splits(data, dates)

periods = 10
x = data.set_index("date")["close"][:-periods//2]
predictor = StockPredictor()
res = predictor.predict_using_auto_arima(x, periods)
sma = StockAnalyzer.get_SMA(data["close"])
Visualizer.show(data, dates, res, sma)
