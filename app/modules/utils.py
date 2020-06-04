import argparse
from datetime import datetime
from datetime import timedelta

import pandas as pd

import modules.stock as stock
import modules.database as database
import modules.sql as sql
import modules.ml_gmm as ml_gmm


def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    args = parser.parse_args()
    return args


def init_stocks_db(config: dict):
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database.initialize_database(database_manager, "stocks")
    database_manager.close_conn()


def upload_this_weeks_stock(config: dict,
                            stock_symbol: str):
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man, stock_symbol, start_date)
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database_manager.connect_db()
    database_manager.df_to_sql(stock_data_frame, "stocks")
    database_manager.close_conn()


def upload_ayear_stock(config: dict,
                       stock_symbol: str):
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man, stock_symbol, start_date)
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database_manager.connect_db()
    database_manager.df_to_sql(stock_data_frame, "stocks")
    database_manager.close_conn()


def search_train_gmm_model(config: dict,
                           table: str):
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database_manager.connect_db()
    stocks: list = database_manager.receive_sql_fetchall(sql.select_all_table(table))
    database_manager.close_conn()
    gmm_ml_manager: ml_gmm.GmmMlManager = ml_gmm.GmmMlManager(pd.DataFrame(stocks), config)
    gmm_ml_manager.preprocess_data()
    gmm_ml_manager.grid_search_gmm()
