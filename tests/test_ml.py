"""
tests for the stock module
"""

import pandas as pd
import app.modules.ml_gmm as ml


def preprocess_data():
    """
    Used to test the basic functionality of get_stock with a start date
    """
    test_dict = {"Open": [1, 2, 3, 4],
                 "High": [1, 2, 3, 4],
                 "Low": [1, 2, 3, 4],
                 "clse": [1, 2, 3, 4],
                 "Volume": [1, 2, 3, 4],
                 "Dividends": [1, 2, 3, 4],
                 "Stock Splits": [1, 2, 3, 4]}
    train_data_frame: pd.DataFrame = pd.DataFrame(test_dict)
    ml_manager: ml.MLManager = ml.MLManager(train_data_frame)
    ml_manager.create_xy()
    ml_manager.create_holdout()
    ml_manager.preprocess_data_pipeline()
    assert not ml_manager.pipeline == None
