"""
intergration tests
"""

from datetime import datetime
from datetime import timedelta

import pandas as pd

import modules.stock as stock
import modules.database as database


def test_get_stock_data():
    """
    Used to test the basic functionality of get_stock
    """
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man, "TSLA", start_date)
    assert not stock_data_frame.empty


def test_initialize_database():
    """
    """
    test_dict = {"Open": 1.2,
                 "High": 1.2,
                 "Low": 1.2,
                 "Close": 1.2,
                 "Volume": 1,
                 "Dividends": 1,
                 "Stock Splits": 1}
    want: pd.Series = pd.DataFrame(test_dict, index=test_dict.keys())
    config_dict: dict = {"ip": "127.0.0.1",
                         "password": "test1234",
                         "username": "test1234",
                         "port": "5432",
                         "database": "test1234"}
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    dataframe: pd.DataFrame = database.initialize_database(database_manager)
    assert dataframe.dtypes.equals(want.dtypes)
