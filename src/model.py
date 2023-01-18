# from lazypredict.Supervised import LazyRegressor
from sklearn.ensemble import RandomForestRegressor


class Model():
    def __init__(self, lazy=False):
        self.lazy = lazy
        if lazy:
            raise NotImplementedError("Lazy models are not yet implemented")
            # self.model = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None)
        else:
            self.model = RandomForestRegressor()

    def fit(self, X_train, y_train, X_test=None, y_test=None):
        if self.lazy:
            if X_test is None or y_test is None:
                raise ValueError("X_test and y_test must be provided for lazy models")
            self.model.fit(X_train, X_test, y_train, y_test)
        else:
            self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)
