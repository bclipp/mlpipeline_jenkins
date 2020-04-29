"""
integration tests
"""

from datetime import datetime
from datetime import timedelta

import pandas as pd

import modules.stock as stock
import modules.database as database
import modules.sql as sql


def test_get_stock_data():
    """
    Used to test the basic functionality of get_stock
    """
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man, "TSLA", start_date)
    assert not stock_data_frame.empty


def test_initialize_database():
    """

    :return:
    """
    test_dict = {"Open": 1.2,
                 "High": 1.2,
                 "Low": 1.2,
                 "Close": 1.2,
                 "Volume": 1,
                 "Dividends": 1,
                 "Stock Splits": 1}
    want: pd.DataFrame = pd.DataFrame(test_dict, index=test_dict.keys())
    config_dict: dict = {"ip": "127.0.0.1",
                         "password": "test1234",
                         "username": "test1234",
                         "port": "5432",
                         "database": "test1234"}
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    dataframe: pd.DataFrame = database.initialize_database(database_manager, "stock2")
    database_manager.send_sql(sql_query=sql.drop_table("stock2"))
    assert dataframe.dtypes.equals(want.dtypes)


def test_database_manager_send_sql():
    """

    :return:
    """
    config_dict: dict = {"ip": "127.0.0.1",
                         "password": "test1234",
                         "username": "test1234",
                         "port": "5432",
                         "database": "test1234"}
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    database_manager.connect_db()
    database_manager.send_sql(sql_query=sql.create_stock_table("stock2"))
    database_manager.send_sql(sql_query="SELECT * FROM stock;")
    database_manager.send_sql(sql_query=sql.drop_table("stock2"))


def test_receive_sql_fetchall():
    """

    :return:
    """
    config_dict: dict = {"ip": "127.0.0.1",
                         "password": "test1234",
                         "username": "test1234",
                         "port": "5432",
                         "database": "test1234"}
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    database_manager.connect_db()
    database_manager.send_sql(sql_query=sql.create_stock_table("stock2"))
    database_manager.receive_sql_fetchall(sql_query="SELECT * FROM stock;")
    database_manager.send_sql(sql_query=sql.drop_table("stock2"))


def test_df_to_sq():
    """

    :return:
    """
    test_dict = {"Open": 1.2,
                 "High": 1.2,
                 "Low": 1.2,
                 "Close": 1.2,
                 "Volume": 1,
                 "Dividends": 1,
                 "Stock Splits": 1}
    data_frame: pd.DataFrame = pd.DataFrame(test_dict, index=test_dict.keys())
    config_dict: dict = {"ip": "127.0.0.1",
                         "password": "test1234",
                         "username": "test1234",
                         "port": "5432",
                         "database": "test1234"}
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    database_manager.connect_db()
    database_manager.send_sql(sql_query=sql.create_stock_table("stock2"))
    database_manager.df_to_sql(data_frame,
                               "stock2")
    database_manager.send_sql(sql_query=sql.drop_table("stock2"))
