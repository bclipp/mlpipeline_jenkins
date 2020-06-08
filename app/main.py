"""
This module is the main entry point for stock related functionality
"""

import app.modules.utils as utils  # type: ignore


def main():
    """
    This function accepts cmd line args needed for choice of action.
        - actions:
            * init_db : setup tables needed for stocks
            * upload_this_weeks_stock:  pull a weeks worth of stock data
            * upload_ayear_stock: pull a year's work of stock data
            * search_train_model: train a gmm model on the stock in the database
    """
    config: dict = {
        "db_ip": "postgres",
        "mlflow_ip": "mlflow",
        "password": "test1234",
        "username": "test1234",
        "port": "5432",
        "database": "test1234",
    }

    args = utils.get_args()
    if args.task:
        if args.task == "init_db":
            utils.init_stocks_db(config)
        elif args.task == "upload_this_weeks_stock":
            utils.upload_this_weeks_stock(config, "TSLA")
        elif args.task == "upload_ayear_stock":
            utils.upload_ayear_stock(config, "TSLA")
        elif args.task == "search_train_model_gmm":
            utils.search_train_gmm_model(config, "stocks")
    else:
        print("no valid arg where provided")


if __name__ == "__main__":
    main()
