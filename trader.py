import json
import requests
import time


class Trader:

    def __init__(self, api_key:str, secret_key:str) -> None:
        self.api_key = api_key
        self.secret_key = secret_key
        self.paper_trade_url = "https://paper-api.alpaca.markets"

    def buy(self, ticker:str, quantity:int) -> json:
        url = f"{self.paper_trade_url}/v2/orders"
        headers = {
            "APCA-API-KEY-ID": self.api_key,
            "APCA-API-SECRET-KEY": self.secret_key
        }
        params = {
            "symbol": ticker,
            "qty": quantity,
            "side": "buy",
            "type": "market",
            "time_in_force": "gtc"
        }
        response = requests.post(url, headers=headers, json=params)
        response = response.json()
        return response

    def sell(self, ticker:str, quantity:int) -> json:
        url = f"{self.paper_trade_url}/v2/orders"
        headers = {
            "APCA-API-KEY-ID": self.api_key,
            "APCA-API-SECRET-KEY": self.secret_key
        }
        params = {
            "symbol": ticker,
            "qty": quantity,
            "side": "sell",
            "type": "market",
            "time_in_force": "gtc"
        }
        response = requests.post(url, headers=headers, json=params)
        response = response.json()
        return response

    def run(self) -> None:
        ticker = "NVDA"
        quantity = 100
        while True:
            self.buy(ticker, quantity)
            time.sleep(10)
            self.sell(ticker, quantity)
