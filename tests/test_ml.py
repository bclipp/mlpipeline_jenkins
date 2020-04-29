"""
tests for the stock module
"""
from unittest.mock import Mock

import pandas as pd
import modules.ml as ml


def test_get_training_data():
    """
    Used to test the basic functionality of get_stock with a start date
    """
    test_dict = {"Open": 1.2,
                 "High": 1.2,
                 "Low": 1.2,
                 "Close": 1.2,
                 "Volume": 1,
                 "Dividends": 1,
                 "Stock Splits": 1}
    train_data_frame: pd.DataFrame = pd.DataFrame(test_dict, index=test_dict.keys())
    ml_manager: Mock()
    got: pd.DataFrame = ml.get_training_data(train_data_frame,
                                                    ml_manager,
                                                    True)
    assert not got.empty

def test_grid_search():

def test_predict():

def test_save_model():