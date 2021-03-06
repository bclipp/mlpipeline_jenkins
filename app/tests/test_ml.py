"""
tests for the stock module
"""
from unittest.mock import Mock  # type: ignore

import pytest  # type: ignore
import pandas as pd  # type: ignore

import app.modules.ml_gmm as ml_gmm  # type: ignore

TEST_DATA = [
    # first test
    # data_frame
    (pd.DataFrame(
        columns=["Open",
                 "High",
                 "Low",
                 "clse",
                 "Volume",
                 "Dividends",
                 "Stock Splits"],
        data=[[1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3]]),
     # wanted
     pd.DataFrame(
         columns=["Open",
                  "High",
                  "Low",
                  "clse",
                  "Volume",
                  "Dividends",
                  "Stock Splits"],
         data=[[1, 2, 0, 3, 4, 5, 3],
               [1, 2, 0, 3, 4, 5, 3],
               [1, 2, 0, 3, 4, 5, 3]])),
    # second test
    # data_frame
    (pd.DataFrame(
        columns=["Open",
                 "High",
                 "Low",
                 "clse",
                 "Volume",
                 "Dividends",
                 "Stock Splits"],
        data=[[1, 2, "a", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3]]),
     # wanted
     pd.DataFrame(
         columns=["Open",
                  "High",
                  "Low",
                  "clse",
                  "Volume",
                  "Dividends",
                  "Stock Splits"],
         data=[[1, 2, 0, 3, 4, 5, 3],
               [1, 2, 1, 3, 4, 5, 3],
               [1, 2, 1, 3, 4, 5, 3]]))
]


@pytest.mark.parametrize("data_frame,wanted", TEST_DATA)
def test_preprocess_data(data_frame, wanted):
    """
    test_preprocess_data is used for  testing that the preprocessing is done correctly.
    Currently there is only label encoding.
    :param data_frame:
    :param wanted:
    :return:
    """
    mlflow = Mock()
    config: dict = {"mlflow_ip": "mlflow"}
    gmm_ml_manager: ml_gmm.GmmMlManager = ml_gmm.GmmMlManager(pd.DataFrame(data_frame),
                                                              config,
                                                              mlflow)
    gmm_ml_manager.preprocess_data()
    got = gmm_ml_manager.train_data_frame_clean
    print(got)
    print(f"sum {got} wanted {wanted}")
    assert got.equals(wanted)


def test_grid_search_gmm():
    """
    test_grid_search_gmm is used to verify that the basic functionality of training
    the GMM model works
    :param data_frame:
    :param wanted:
    :return:
    """
    data_frame = pd.DataFrame(
        columns=["Open",
                 "High",
                 "Low",
                 "clse",
                 "Volume",
                 "Dividends",
                 "Stock Splits"],
        data=[[1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3]])
    mlflow = Mock()
    config: dict = {"mlflow_ip": "mlflow"}
    gmm_ml_manager: ml_gmm.GmmMlManager = ml_gmm.GmmMlManager(pd.DataFrame(data_frame),
                                                              config,
                                                              mlflow)
    gmm_ml_manager.preprocess_data()
    gmm_ml_manager.grid_search_gmm()
