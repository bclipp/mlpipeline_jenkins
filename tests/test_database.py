"""

"""
import pandas as pd

import modules.database as database


def test_initialize_database():
    """
    """
    test_dict = {"Open":1.2,
                 "High":1.2,
                 "Low":1.2,
                 "Close":1.2,
                 "Volume":1,
                 "Dividends":1,
                 "Stock Splits":1}
    want:pd.Series = pd.DataFrame(test_dict,index=test_dict.keys())
    config_dict:dict = {"ip":"127.0.0.1",
                        "password":"test1234",
                        "username":"test1234",
                        "port": "5432",
                        "database":"test1234"}
    database_manager:database.DatabaseManager = database.DatabaseManager(config_dict)
    dataframe: pd.DataFrame = database.initialize_database(database_manager)
    assert dataframe.dtypes.equals(want.dtypes)
