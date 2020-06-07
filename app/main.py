"""
This module is the main entry point for stock related functionality
"""

import modules.utils as utils


def main():
    """
    This function accepts cmd line args needed for choice of action.
    """
    config: dict = {"db_ip": "postgres",
                    "mlflow_ip": "mlflow",
                    "password": "test1234",
                    "username": "test1234",
                    "port": "5432",
                    "database": "test1234"}

    args = utils.get_args()
    if args.task:
        if args.task == "init_db":
            utils.init_stocks_db(config)
        elif args.task == "upload_this_weeks_stock":
            utils.upload_this_weeks_stock(config, "TSLA")
        elif args.task == "upload_ayear_stock":
            utils.upload_ayear_stock(config, "TSLA")
        elif args.task == "search_train_model":
            utils.search_train_gmm_model(config, "stocks")
    else:
        print("no valid arg where provided")


if __name__ == "__main__":
    main()
