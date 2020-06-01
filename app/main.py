import argparse
from datetime import datetime
from datetime import timedelta

import pandas as pd

import app.stock as stock
import app.database as database
import app.sql as sql
import app.ml as ml


def upload_this_weeks_stock(config_dict: dict,
                            stock_symbol: str):
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man, stock_symbol, start_date)
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    database_manager.connect_db()
    database_manager.df_to_sql(stock_data_frame, "stocks")
    database_manager.close_conn()


def upload_ayear_stock(config_dict: dict,
                       stock_symbol: str):
    start_date: str = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    stock_data_frame: pd.DataFrame = stock.get_stock(stock.stock_man, stock_symbol, start_date)
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    database_manager.connect_db()
    database_manager.df_to_sql(stock_data_frame, "stocks")
    database_manager.close_conn()


def train_model(config_dict: dict,
                table: str):
    database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
    stocks: list = database_manager.receive_sql_fetchall(sql.select_all_table(table))
    ml_manager: ml.MLManager = ml.MLManager(pd.DataFrame(stocks))
    ml_manager.create_xy()
    ml_manager.create_holdout()
    ml_manager.grid_search()
    ml_manager.train_cv()


def main():
    config_dict: dict = {"ip": "127.0.0.1",
                         "password": "test1234",
                         "username": "test1234",
                         "port": "5432",
                         "database": "test1234"}
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    run_option = False
    run_option = args.run_option

    if run_option == "init_db":
        database_manager: database.DatabaseManager = database.DatabaseManager(config_dict)
        database.initialize_database(database_manager, "stocks")
        database_manager.close_conn()
    elif run_option == "upload_this_weeks_stock":
        upload_this_weeks_stock(config_dict, "TSLA")
    elif run_option == "upload_ayear_stock":
        upload_ayear_stock(config_dict, "TSLA")
    elif run_option == "train_model":
        train_model(config_dict, "stock")
    elif run_option is False:
        print("error can't read run command")
    else:
        print("no valid arg where provided")


if __name__ == "__main__":
    main()
