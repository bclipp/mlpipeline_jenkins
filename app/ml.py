"""
Used for ML realated code

"""
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
import pandasas pd


class MLManager():

    def __init__(self, train_data_frame):
        self.train_data_frame = train_data_frame
        self.X_train_holdout = None
        self.X_test_holdout = None
        self.y_train_holdout = None
        self.y_test_holdout = None
        self.X = None
        self.y = None
        self.param_grid = None
        self.en = None
        self.cv = None
        self.scaled_train_dataframe = None

    def preprocess_data(self):
        scaler = StandardScaler()
        self.scaled_train_dataframe: pd.DataFrame = scaler.fit_transform(self.train_data_frame)

    def create_xy(self):
        self.X = self.train_data_frame.drop(['clse'], axis=1).reset_index(drop=True)
        self.y = self.train_data_frame["clse"].reset_index(drop=True)

    def create_holdout(self):
        self.X_train_holdout, \
        self.X_test_holdout, \
        self.y_train_holdout, \
        self.y_test_holdout = train_test_split(self.X,
                                               self.y,
                                               test_size=0.20,
                                               random_state=42)


    def grid_search(self):
        self.en = ElasticNet(random_state=42)
        self.param_grid = {"max_iter": [1, 5],
                           "alpha": [0.0001, 0.001, 0.01],
                           "l1_ratio": np.arange(0.0, 1.0, 0.1)}
        self.en_random = RandomizedSearchCV(estimator=self.en,
                                            param_distributions=self.param_grid,
                                            n_iter=100,
                                            cv=3,
                                            verbose=2,
                                            random_state=42,
                                            n_jobs=-1)

    def train_cv(self):
        self.en_random.fit(self.X_train_holdout,
                           self.y_train_holdout)
        print(self.en_random.best_params_)
        print(self.en_random.best_score_)

    def predict_holdout(self,
                data: int):
        return self.en_random.predict(self.X_test_holdout)

    def save_model(self,
                   url: str):

        with open(url, 'wb') as file:
            pickle.dump(self.cv, file)

