"""
tests for the stock module
"""
from unittest.mock import Mock  # type: ignore

import pandas as pd  # type: ignore
import app.modules.mlflow as mlflow # type: ignore

import app.modules.ml_gmm as ml_gmm  # type: ignore


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
    config: dict = {"mlflow_ip": "mlflow"}
    mlflow_manager = mlflow.MlFlowManager(config["ip"],
                                          "intergration_test")
    config: dict = {"mlflow_ip": "mlflow"}
    gmm_ml_manager: ml_gmm.GmmMlManager = ml_gmm.GmmMlManager(pd.DataFrame(data_frame),
                                                              config,
                                                              mlflow)
    gmm_ml_manager.preprocess_data()
    gmm_ml_manager.grid_search_gmm()
