import pandas as pd
import requests
from dateutil.parser import parse


class StockFetcher:

    def __init__(self, api_key: str, secret_key: str) -> None:
        self.api_key = api_key
        self.secret_key = secret_key
        self.data_url = "https://data.alpaca.markets"

    def get_data(
        self,
        ticker: str,
        start_date: str,
        end_date: str,
        timeframe: str = "1Day",
        limit: int = 10000,
    ) -> list:
        url = f"{self.data_url}/v2/stocks/{ticker}/bars"
        headers = {
            "APCA-API-KEY-ID": self.api_key,
            "APCA-API-SECRET-KEY": self.secret_key,
        }
        params = {
            "start": start_date,
            "end": end_date,
            "timeframe": timeframe,
            "limit": limit,
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise ValueError(response.status_code)
        data = response.json()
        return data["bars"]

    def format_data(self, data: list) -> pd.DataFrame:
        formatted_data = []
        for item in data:
            formatted_item = {
                "date": parse(item["t"]).strftime("%Y-%m-%d"),
                "open": item["o"],
                "high": item["h"],
                "low": item["l"],
                "close": item["c"],
                "volume": item["v"],
            }
            formatted_data.append(formatted_item)
        formatted_data = pd.DataFrame(formatted_data)
        return formatted_data
