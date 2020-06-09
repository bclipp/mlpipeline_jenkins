"""
tests for the stock module
"""
import pandas as pd  # type: ignore
import app.modules.mlflow as mlflow # type: ignore

import app.modules.ml_gmm as ml_gmm  # type: ignore


def test_mlflow_intergration():
    """
    Used to test that mlflow is working
    :param data_frame:
    :param wanted:
    :return:
    """
    data_frame_intergration: pd.DataFrame = pd.DataFrame(
        columns=["Open", "High", "Low", "clse", "Volume", "Dividends", "Stock Splits"],
        data=[[5, 2, "b", 3, 4, 5, 3],
              [7, 2, "b", 3, 4, 5, 3],
              [8, 2, "b", 3, 4, 5, 3],
              [3, 2, "b", 3, 4, 5, 3],
              [2, 2, "b", 3, 4, 5, 3],
              [8, 2, "b", 3, 4, 5, 3],
              [2, 2, "b", 3, 4, 5, 3],
              [8, 2, "b", 3, 4, 5, 3],
              [19, 2, "b", 3, 4, 5, 3],
              [53, 2, "b", 3, 4, 5, 3],
              [11, 2, "b", 3, 4, 5, 3],
              [16, 2, "b", 3, 4, 5, 3]])
    config: dict = {"mlflow_ip": "127.0.0.1"}
    mlflow_manager = mlflow.MlFlowManager(config["ip"],
                                          "intergration_test")
    config: dict = {"mlflow_ip": "mlflow"}
    gmm_ml_manager: ml_gmm.GmmMlManager = ml_gmm.GmmMlManager(pd.DataFrame(data_frame_intergration),
                                                              config,
                                                              mlflow_manager)
    gmm_ml_manager.preprocess_data()
    gmm_ml_manager.grid_search_gmm()
