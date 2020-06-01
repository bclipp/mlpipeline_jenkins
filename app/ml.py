"""
Used for ML realated code

"""
from sklearn import mixture
import mlflow
from urllib.parse import urlparse


class MLManager():

    def __init__(self, train_data_frame):
        self.train_data_frame = train_data_frame
        self.X = None
        self.model = None

    def preprocess_data(self):
        print("label incode only non numeric")

    def grid_search_gmm(self):
        with mlflow.start_run():
            for x in range(10):
                n_components = x
                model = mixture.GaussianMixture(n_components=n_components, covariance_type='full')
                model.fit(self.X)
                aic = model.aic()
                bic = model.bic()
                print("aic: " + aic)
                print("bic: " + bic)
                mlflow.log_param("n_components", x)
                mlflow.log_param("covariance_type", "full")
                mlflow.log_metric("aic", aic)
                mlflow.log_metric("bic", bic)

    def train_gmm(self):
        with mlflow.start_run():
            n_components = self.n_components_best
            model = mixture.GaussianMixture(n_components=n_components, covariance_type='full')
            model.fit(self.X)
            aic = model.aic()
            bic = model.bic()
            print("aic: " + aic)
            print("bic: " + bic)
            mlflow.log_param("n_components", n_components)
            mlflow.log_param("covariance_type", "full")
            mlflow.log_metric("aic", aic)
            mlflow.log_metric("bic", bic)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="gmm")
            else:
                mlflow.sklearn.log_model(model, "model")
            self.model = model
