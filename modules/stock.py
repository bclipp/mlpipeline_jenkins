"""
This module is used for interacting with stock data
"""

from typing import Callable
from datetime import datetime, timedelta

import pandas as pd  # type: ignore
import yfinance as yf  # type: ignore


def stock_man(stock_symbol: str, today: str, start_date: str = None)-> pd.DataFrame:
    """

    :param stock_symbol:
    :param start_date:
    :return:
    """
    ticker: yf.Ticker = yf.Ticker(stock_symbol)
    data_frame: pd.DataFrame = ticker.history(period="1d", start=start_date, end=today)
    return data_frame


def get_stock(stock_manager: Callable,
              stock_symbol: str,
              start_date: str = None) -> pd.DataFrame:
    """
    start_date: start date to pull stock data, in YYYY-MM-DD
    stock_name: company to lookup stock data
    :return:
    """
    if not start_date:
        start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    today: str = datetime.today().strftime('%Y-%m-%d')
    data_frame: pd.DataFrame = stock_manager(stock_symbol, today, start_date)
    return data_frame
