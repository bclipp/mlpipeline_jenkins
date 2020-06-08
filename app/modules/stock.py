"""
This module is used for interacting with stock data
"""

from typing import Callable  # type: ignore
from datetime import datetime  # type: ignore

import pandas as pd  # type: ignore
import yfinance as yf  # type: ignore


def stock_man(stock_symbol: str,
              end: str,
              start_date: str = None) -> pd.DataFrame:
    """
    stock_man used manage interactions with yfinance

    :param stock_symbol: stock symbol to download
    :param today: tdate to end lookup process
    :param start_date: date to start the lookup process.
    :return:
    """
    ticker: yf.Ticker = yf.Ticker(stock_symbol)
    data_frame: pd.DataFrame = ticker.history(period="1d", start=start_date, end=end)
    return data_frame


def get_stock(
        stock_manager: Callable,
        stock_symbol: str,
        start_date: str) -> pd.DataFrame:
    """
    get_stock is a wrapper to download stock data

    stock_manager: object to interact with y finance
    start_date: start date to pull stock data, in YYYY-MM-DD
    stock_symbol: company to lookup stock data
    :return: a df with date, open , high , low, Dividends, stock splits, and symbol
    """
    today: str = datetime.today().strftime("%Y-%m-%d")
    ticker: yf.Ticker = yf.Ticker(stock_symbol)
    data_frame: pd.DataFrame = stock_manager(stock_symbol, today, start_date)
    data_frame["symbol"] = stock_symbol
    data_frame = data_frame.reset_index()
    data_frame["Date"] = pd.to_datetime(data_frame["Date"]).dt.date
    data_frame["date_symbol"] = data_frame["symbol"] + "_" + data_frame["Date"].map(str)
    data_frame["clse"] = data_frame["Close"]
    data_frame["Stock_Splits"] = data_frame["Stock Splits"]
    data_frame = data_frame.drop(["Close", "Stock Splits"], axis=1)
    return data_frame
