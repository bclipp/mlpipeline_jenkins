"""
tests for the stock module
"""
from unittest.mock import Mock  # type: ignore

import pytest  # type: ignore
import pandas as pd  # type: ignore

import app.modules.ml_gmm as ml_gmm  # type: ignore

test_data = [
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
               [1, 2, 0, 3, 4, 5, 3]]))]


@pytest.mark.parametrize("data_frame,wanted", test_data)
def test_preprocess_data_2(data_frame, wanted):
    """

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
