import modules.utils as utils


def main():
    # replace with env var
    config: dict = {"db_ip": "127.0.0.1",
                    "mlflow_ip": "127.0.0.1",
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
