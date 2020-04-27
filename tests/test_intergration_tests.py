"""
intergration tests
"""

from datetime import datetime
from datetime import date, timedelta

import pandas as pd
import modules.stock as stock


def test_get_stock_data():
    """
    Used to test the basic functionality of get_stock
    """
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man(), "TSLA", start_date)
    assert not stock_data_frame.empty
