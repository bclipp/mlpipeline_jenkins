"""
this module is used for interacting with the mlflow server
"""

import mlflow.sklearn  # type: ignore
import mlflow  # type: ignore


class MlFlowManager:
    """
    Used for interacting with MLflow server.
    """

    def __init__(self, ip_address: str,
                 experiment_name: str):
        """

        :param ip_address: address of mlflow server
        :param experiment_name: name to log on server
        """
        self.ip_address = ip_address
        mlflow.set_tracking_uri(f"http://{ip_address}:5000/")
        mlflow.set_experiment("/" + experiment_name)

    def start_run(self, name: str):
        """
        start_run is used for organizing ml experiments

        :param name:  used when logging to mlflow server
        :return:
        """
        mlflow.start_run(run_name=name)

    def end_run(self):
        """
        end_run is used for organizing ml experiments
        :return:
        """
        mlflow.end_run()

    def set_tag(self,
                key: str,
                value: str):
        """

        :param key: metadata about the run
        :param value: metadata about the run
        :return:
        """

    def log_param(self,
                  key: str,
                  value):
        """

        :param key: metadata about model
        :param value: metadata about model
        :return:
        """
        mlflow.log_param(key, value)

    def sk_log_model(self,
                     model,
                     name: str):
        """

        :param model: trained model to log
        :param name: name to use for the model
        :return:
        """
        mlflow.sklearn.log_model(model, name)

    def sk_save_model(self,
                      model,
                      path: str,
                      serialization_format: str):
        """

        :param model:  trained model to save
        :param path: path to save locally, you can't save a model to the same location.
        :param serialization_format: method to use for serialization when saving
        :return:
        """
        mlflow.sk_save_model(model,
                             path=path,
                             serialization_format=serialization_format)


