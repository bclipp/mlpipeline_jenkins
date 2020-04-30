"""
tests for the stock module
"""
from unittest.mock import Mock
from datetime import datetime, timedelta

import pandas as pd
import app.stock as stock


def test_get_stock_start_date():
    """
    Used to test the basic functionality of get_stock with a start date
    """
    stock_manager_mock: Mock = Mock()
    fake_dict = {"test": "test"}
    stock_manager_mock.return_value = pd.DataFrame(fake_dict, index=fake_dict.keys())
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock_manager_mock, "TSLA", start_date)
    assert not stock_data_frame.empty


def test_get_stock():
    """
    Used to test the basic functionality of get_stock
    """
    stock_manager_mock: Mock = Mock()
    fake_dict = {"test": "test"}
    stock_manager_mock.return_value = pd.DataFrame(fake_dict, index=fake_dict.keys())
    stock_data_frame: pd.DataFrame = stock.get_stock(stock_manager_mock, "TSLA")
    assert not stock_data_frame.empty


def test_get_stock_initial():
    """
    Used to test the basic functionality of get_stock
    """
    stock_manager_mock: Mock = Mock()
    fake_dict = {"test": "test"}
    stock_manager_mock.return_value = pd.DataFrame(fake_dict, index=fake_dict.keys())
    stock_data_frame: pd.DataFrame = stock.get_stock(stock_manager_mock, "TSLA")
    assert not stock_data_frame.empty