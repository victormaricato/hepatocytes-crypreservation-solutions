# from lazypredict.Supervised import LazyRegressor
from typing import Literal

from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor

models = {
    "Linear Regression": LinearRegression
    , "Ridge": Ridge
    , "Lasso": Lasso
    , "ElasticNet": ElasticNet
    , "KNeighborsRegressor": KNeighborsRegressor
    , "SVR": SVR
    , "RandomForestRegressor": RandomForestRegressor
    , "ExtraTreesRegressor": ExtraTreesRegressor
    , "XGBRegressor": XGBRegressor
}


class Model:
    def __init__(self, model_class: Literal[
        "Linear Regression", "Ridge", "Lasso", "ElasticNet", "KNeighborsRegressor", "SVR", "RandomForestRegressor",
        "ExtraTreesRegressor", "XGBRegressor"
    ]):
        self.model = models[model_class]()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)
