"""
Used for ML realated code

"""
from sklearn import mixture
import mlflow
from urllib.parse import urlparse
from sklearn.preprocessing import LabelEncoder
from pandas.api.types import is_numeric_dtype


class MLManager():

    def __init__(self, train_data_frame):
        self.train_data_frame = train_data_frame
        self.train_data_frame_clean = None
        self.X = None
        self.model = None

    def preprocess_data(self):
        data_frame = self.train_data_frame.copy()
        threshold = len(data_frame) * 1
        data_frame = data_frame.dropna(thresh=threshold,
                                       axis=1)
        le = LabelEncoder()

        def emcode_me(column):
            if not is_numeric_dtype(column):
                return le.fit_transform(column.astype(str))
            else:
                return column
        self.train_data_frame_clean = data_frame.apply(lambda column: emcode_me(column), axis=0, result_type="expand")

    def grid_search_gmm(self):
        with mlflow.start_run():
            x = self.train_data_frame_clean
            for i in range(1, 10):
                n_components = i
                model = mixture.GaussianMixture(n_components=n_components, covariance_type='full')
                model.fit(x)
                aic = model.aic(x)
                bic = model.bic(x)
                print("aic: " + aic)
                print("bic: " + bic)
                mlflow.log_param("n_components", x)
                mlflow.log_param("covariance_type", "full")
                mlflow.log_metric("aic", aic)
                mlflow.log_metric("bic", bic)

    def train_gmm(self,
                  n_components=1,
                  covariance_type="full"):
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
