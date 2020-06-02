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
    gmm_ml_manager: ml_gmm.GmmMlManager = ml_gmm.GmmMlManager(pd.DataFrame(stocks,config))
    gmm_ml_manager.preprocess_data()
    gmm_ml_manager.grid_search_gmm()


# please reformat so data isn't pulled more than once for search and train
def main():
    # replace with env var
    config: dict = {"ip": "postgres",
                    "password": "test1234",
                    "username": "test1234",
                    "port": "5432",
                    "database": "test1234"}

    args = get_args()
    if args.task:
        if args.task == "init_db":
            init_stocks_db(config)
        elif args.task == "upload_this_weeks_stock":
            upload_this_weeks_stock(config, "TSLA")
        elif args.task == "upload_ayear_stock":
            upload_ayear_stock(config, "TSLA")
        elif args.task == "search_train_model":
            search_train_gmm_model(config, "stocks")
    else:
        print("no valid arg where provided")


if __name__ == "__main__":
    main()
