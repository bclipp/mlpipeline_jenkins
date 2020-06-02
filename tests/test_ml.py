"""
tests for the stock module
"""
from unittest.mock import Mock

import pandas as pd
import app.ml_gmm as ml


def test_create_xy():
    """
    Used to test the basic functionality of get_stock with a start date
    """
    test_dict = {"Open": [1,2,3,4],
                 "High": [1,2,3,4],
                 "Low": [1,2,3,4],
                 "clse": [1,2,3,4],
                 "Volume": [1,2,3,4],
                 "Dividends": [1,2,3,4],
                 "Stock Splits": [1,2,3,4]}
    train_data_frame: pd.DataFrame = pd.DataFrame(test_dict)
    ml_manager: ml.MLManager = ml.MLManager(train_data_frame)
    ml_manager.create_xy()
    assert not ml_manager.X == None
    # add or y

def test_create_holdout():
    """
    Used to test the basic functionality of get_stock with a start date
    """
    test_dict = {"Open": [1,2,3,4],
                 "High": [1,2,3,4],
                 "Low": [1,2,3,4],
                 "clse": [1,2,3,4],
                 "Volume": [1,2,3,4],
                 "Dividends": [1,2,3,4],
                 "Stock Splits": [1,2,3,4]}
    train_data_frame: pd.DataFrame = pd.DataFrame(test_dict)
    ml_manager: ml.MLManager = ml.MLManager(train_data_frame)
    ml_manager.create_xy()
    ml_manager.create_holdout()
    assert not ml_manager.X_train_holdout == None
    # rest of vars

def test_preprocess_data_pipeline():
    """
    Used to test the basic functionality of get_stock with a start date
    """
    test_dict = {"Open": [1,2,3,4],
                 "High": [1,2,3,4],
                 "Low": [1,2,3,4],
                 "clse": [1,2,3,4],
                 "Volume": [1,2,3,4],
                 "Dividends": [1,2,3,4],
                 "Stock Splits": [1,2,3,4]}
    train_data_frame: pd.DataFrame = pd.DataFrame(test_dict)
    ml_manager: ml.MLManager = ml.MLManager(train_data_frame)
    ml_manager.create_xy()
    ml_manager.create_holdout()
    ml_manager.preprocess_data_pipeline()
    assert not ml_manager.pipeline == None


def test_grid_search():
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
    ml_manager.grid_search()
    assert not ml_manager.cv == None

def train_cv():
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
    ml_manager.grid_search()
    ml_manager.train_cv()
    assert not ml_manager.cv == None


def test_predict():
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
    ml_manager.grid_search()
    ml_manager.train_cv()
    ml_manager.predict(234)
