import os

from stock_analyzer import StockAnalyzer
from stock_fetcher import StockFetcher
from stock_predictor import StockPredictor
from trader import Trader
from visualizer import Visualizer

api_key = os.environ["ALPACA_API_KEY"]
secret_key = os.environ["ALPACA_SECRET_KEY"]
ticker = "AAPL"
# start_date = "2020-01-01"
# end_date = "2024-07-19"

# fetcher = StockFetcher(api_key, secret_key)
# raw_data = fetcher.get_data(ticker, start_date, end_date)
# data = fetcher.format_data(raw_data)
# dates = StockAnalyzer.get_split_dates(ticker, start_date, end_date)
# data = StockAnalyzer.adjust_for_stock_splits(data, dates)
# print("DATA")
# print(data)

# rsi = StockAnalyzer.get_RSI(data["close"])
# print("RSI")
# print(rsi.iloc[-1])

# print("SMA")
# sma = StockAnalyzer.get_SMA(data["close"])
# for window, val in sma.items():
#     print(window, val.iloc[-1])

# print("EMA")
# ema = StockAnalyzer.get_EMA(data["close"])
# for window, val in ema.items():
#     print(window, val.iloc[-1])

# streamlit run test.py
# Visualizer.show(data, dates)

trader = Trader(api_key, secret_key)
trader.run()