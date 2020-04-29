from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV


import pandas as pd

class MLManager():

    def __init__(self, train_data_frame):
        self.train_data_frame = train_data_frame
        self.X = None
        self.y = None
        self.preprocessor = None
        self.param_grid = None

    def create_xy(self):
        self.X = self.train_data_frame.drop(['clse'],axis=1)
        self.y = self.train_data_frame["clse"]

    def preprocess_data(self):
        numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())])
        numeric_features = numeric_features = self.X.select_dtypes(include=['int64', 'float64']).columns
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features)])
        self.en = Pipeline(steps=[('preprocessor', self.preprocessor),
                             ('regressor', ElasticNet())])

    def grid_search(self):
        self.param_grid = {
            'alpha': [200, 500],
            'l1_ratio': [],
            'classifier__max_depth': [4, 5, 6, 7, 8],
            'classifier__criterion': ['gini', 'entropy']}
        self.CV = GridSearchCV(self.en, self.param_grid, n_jobs=1)

    def train_cv(self):
        self.CV.fit(self.X, self.Y)
        print(self.CV.best_params_)
        print(self.CV.best_score_)

    def predict(self):




def get_training_data(train_data_frame: pd.DataFrame,
                      ml_manager:MLManager,
                      preposessing=True):

    #