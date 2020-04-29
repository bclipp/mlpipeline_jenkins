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
    ml_manager: Mock()
    data_frame: pd.DataFrame = ml.get_training_data(ml_manager,
                                                    preposessing=True)
    assert not data_frame.empty

def test_grid_search():

def test_predict():
    
def test_save_model():