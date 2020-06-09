"""
This module contains all GMM ML related code
"""
from sklearn import mixture  # type: ignore
from sklearn.preprocessing import LabelEncoder  # type: ignore
import pandas as pd  # type: ignore
from pandas.api.types import is_numeric_dtype  # type: ignore

import app.modules.mlflow as mlflow


class GmmMlManager:
    """
    GmmMlManager is used for training GMM models and searching different hyperparameters.
    """

    def __init__(self, train_data_frame: pd.DataFrame, config: dict, mlflow):
        """

        :param train_data_frame: data used for trainig the model
        :param config: configuration of most related to MLflow
        """
        self.mlflow = mlflow
        self.config = config
        self.train_data_frame = train_data_frame
        self.train_data_frame_clean = None
        self.model = None
        ip_address = self.config["mlflow_ip"]
        self.mlflow.set_tracking_uri(f"http://{ip_address}:5000/")
        self.mlflow.set_experiment("/mlflow_gmm")

    def preprocess_data(self):
        """
        preprocess_data is used for prepossessing the training data.
        Data Processing is limited to label encoding. scaling might be a good idea
        to add in the future.

        :return:
        """
        data_frame = self.train_data_frame.copy()
        threshold = len(data_frame) * 1
        data_frame = data_frame.dropna(thresh=threshold, axis=1)
        label_encoder = LabelEncoder()

        def encode_me(column):
            if not is_numeric_dtype(column):
                return label_encoder.fit_transform(column.astype(str))
            return column

        self.train_data_frame_clean = data_frame.apply(encode_me, axis=0, result_type="expand")

    def grid_search_gmm(self):
        """
        grid_search_gmm ia used to train a range of models and upload the metrics & models.
        :return:
        """
        x_train = self.train_data_frame_clean
        for i in range(1, 10):
            self.mlflow.start_run(run_name="Grid Search GMM n_component: " + str(i))
            self.mlflow.set_tag("mlflow.note.content",
                                "Training a range of cluster sizes, 1-10.")
            self.mlflow.set_tag("mlflow.user", "Brian Lipp")
            self.mlflow.set_tag("mlflow.source.type", "JOB")
            self.mlflow.set_tag("mlflow.source.name", "Jenkins ML Pipeline")
            self.mlflow.set_tag("mlflow.source.git.repoURL",
                                "https://github.com/bclipp/mlpipeline_jenkins")
            n_components = i
            model = mixture.GaussianMixture(n_components=n_components,
                                            covariance_type="full")
            model.fit(x_train)
            aic = str(model.aic(x_train))
            bic = str(model.bic(x_train))
            print("aic: " + aic)
            print("bic: " + bic)
            self.mlflow.log_param("n_components", i)
            self.mlflow.log_param("covariance_type", "full")
            self.mlflow.log_metric("aic", float(aic))
            self.mlflow.log_metric("bic", float(bic))
            self.mlflow.sk_log_model(model, "gmm_n_component_" + str(i))
            self.mlflow.sklearn.save_model(model,
                                           path="model_gmm_" + str(i),
                                           serialization_format=mlflow.sklearn.SERIALIZATION_FORMAT_PICKLE)
            self.mlflow.end_run()
