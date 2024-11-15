import pandas as pd
import requests
import sqlalchemy as sa
from dateutil.parser import parse
from .stock_data import StockData


class StockDataManager:

    def __init__(
        self,
        db_user: str,
        db_password: str,
        db_host: str,
        db_port: str,
        db_name: str,
        alpaca_api_key: str,
        alpaca_secret_key: str,
    ) -> None:

        self.engine_url = sa.engine.URL.create(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name,
        )

        self.engine = sa.create_engine(url=self.engine_url)

        self.alpaca_api_key = alpaca_api_key
        self.alpaca_secret_key = alpaca_secret_key
        self.alpaca_data_url = "https://data.alpaca.markets"

    def save_to_db(self, stock_data: StockData) -> None:

        try:

            curr_data = pd.read_sql(stock_data.ticker, self.engine)
            combined_data = (
                pd.concat([curr_data, stock_data.data])
                .drop_duplicates(subset=["date"])
                .sort_values("date")
            )
            combined_data.to_sql(
                name=stock_data.ticker,
                con=self.engine,
                if_exists="replace",
                index=False,
            )

        except:

            stock_data.data.to_sql(
                name=stock_data.ticker,
                con=self.engine,
                if_exists="replace",
                index=False,
            )

    def load_from_db(self, ticker: str) -> StockData:

        data = None

        try:

            data = pd.read_sql_table(table_name=ticker, con=self.engine)

        except Exception as e:

            print(e)

        return StockData(ticker=ticker, data=data)

    def get_data_from_alpaca(
        self,
        ticker: str,
        start_date: str,
        end_date: str,
        timeframe: str = "1Day",
        limit: int = 10000,
    ) -> StockData:

        url = f"{self.alpaca_data_url}/v2/stocks/{ticker}/bars"

        headers = {
            "APCA-API-KEY-ID": self.alpaca_api_key,
            "APCA-API-SECRET-KEY": self.alpaca_secret_key,
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

        return StockData(ticker=ticker, data=pd.DataFrame(data["bars"]))

    def format_data(self, stock_data: StockData) -> StockData:

        formatted = stock_data.data[["t", "o", "h", "l", "c", "v"]]
        formatted.columns = ["date", "open", "high", "low", "close", "volume"]
        formatted.loc[:, "date"] = formatted["date"].apply(lambda x: parse(x).date())

        return StockData(ticker=stock_data.ticker, data=formatted)
