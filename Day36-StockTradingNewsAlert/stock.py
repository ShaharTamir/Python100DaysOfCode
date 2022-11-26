import requests
import os
from datetime import datetime, timedelta

STOCKS_API_KEY = os.environ.get("STOCK_DATA_PASS")
KEY_FOR_STOCKS = "Time Series (Daily)"


class Stock:

    def __init__(self, symbol: str):
        raw_data = Stock.get_stock_data(symbol)
        parsed_data = Stock.parse_stock_data(raw_data)
        self.close = parsed_data["today"]["close"]
        self.change = float(parsed_data["today"]["close"]) - float(parsed_data["yesterday"]["close"])
        self.average_change = self.change / float(parsed_data["today"]["close"]) * 100
        self.highest = parsed_data["today"]["high"]
        self.lowest = parsed_data["today"]["low"]

    def __str__(self):
        if self.change > 0:
            arrow = "\U0001F53C"
        else:
            arrow = "\U0001F53D"
        return f"""close: ${self.close}\nchange: ${self.change:.3f} {arrow}
change in average: %{self.average_change:.3f}\nhigh: ${self.highest}\nlow: ${self.lowest}"""

    @staticmethod
    def get_stock_data(symbol: str):
        """
        :param symbol: string symbol of stock as appears in stock market
        :return: object with average_change, change from the day before, highest and lowest of today.s
        """
        stocks_url = "https://www.alphavantage.co/query"
        stocks_params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "outputsize": "compact",
            "apikey": STOCKS_API_KEY
        }

        response = requests.get(stocks_url, params=stocks_params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def parse_stock_data(raw_data):
        """
        :param raw_data: json raw stocks data from alphavantage query
        :return: two keys dictionary - today and yesterday. with parsed data
        """
        today_date = datetime.today().date() - timedelta(days=1)
        yesterday = today_date - timedelta(days=1)
        two_days_data = {
            "today": Stock.parse_stock_day_data(raw_data[KEY_FOR_STOCKS][f'{today_date}']),
            "yesterday": Stock.parse_stock_day_data(raw_data[KEY_FOR_STOCKS][f'{yesterday}'])
        }

        return two_days_data

    @staticmethod
    def parse_stock_day_data(raw_day_data):
        day_data = {}
        for key in raw_day_data.keys():
            day_data[key[key.find(".") + 2:]] = raw_day_data[key]

        return day_data

