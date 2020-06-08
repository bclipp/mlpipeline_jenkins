"""
This module will hold general functions used by main
"""

import argparse  # type: ignore
from datetime import datetime  # type: ignore
from datetime import timedelta  # type: ignore

import pandas as pd  # type: ignore

import modules.stock as stock  # type: ignore
import modules.database as database  # type: ignore
import modules.sql as sql  # type: ignore
import modules.ml_gmm as ml_gmm  # type: ignore


def get_args():
    """
    get_args returns the arguments passed
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    args = parser.parse_args()
    return args


def init_stocks_db(config: dict):
    """
    init_stocks_db used for setting up the database
    :param config: config used to access DB
    :return:
    """
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database.initialize_database(database_manager, "stocks")
    database_manager.close_conn()


def upload_this_weeks_stock(config: dict,
                            stock_symbol: str):
    """
    upload_this_weeks_stock is used to download the weeks stock data
    :param config: config used to access DB
    :param stock_symbol: stock company to download
    :return:
    """
    start_date: str = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d")
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man,
                                                     stock_symbol,
                                                     start_date)
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database_manager.connect_db()
    database_manager.df_to_sql(stock_data_frame, "stocks")
    database_manager.close_conn()


def upload_ayear_stock(config: dict,
                       stock_symbol: str):
    """
    upload_ayear_stock is used to download the years stock data
    :param config: config used to access DB
    :param stock_symbol: stock company to download
    :return:
    """
    start_date: str = (datetime.today() - timedelta(days=360)).strftime("%Y-%m-%d")
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man,
                                                     stock_symbol,
                                                     start_date)
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database_manager.connect_db()
    database_manager.df_to_sql(stock_data_frame, "stocks")
    database_manager.close_conn()


def search_train_gmm_model(config: dict,
                           table: str):
    """
    search_train_gmm_model is used to get all the metrics for gmm models on stock data
    :param config: config used to access DB
    :param table: table that has stck data
    :return:
    """
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database_manager.connect_db()
    stocks: list = database_manager.receive_sql_fetchall(sql.select_all_table(table))
    database_manager.close_conn()
    gmm_ml_manager: ml_gmm.GmmMlManager = ml_gmm.GmmMlManager(
        pd.DataFrame(stocks), config
    )
    gmm_ml_manager.preprocess_data()
    gmm_ml_manager.grid_search_gmm()
