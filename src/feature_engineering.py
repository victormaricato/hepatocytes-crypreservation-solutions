from typing import Literal

import pandas as pd

from src.constants import CATEGORICAL_COLUMNS, NUMERICAL_COLUMNS, MISCELLANEOUS_COLUMNS, LABEL_COLUMNS, LABEL


class FeaturePreprocessor:
    CATEGORICAL_FEATURES = set(CATEGORICAL_COLUMNS) - set(MISCELLANEOUS_COLUMNS)
    NUMERICAL_FEATURES = set(NUMERICAL_COLUMNS) - set(LABEL_COLUMNS)
    FEATURES = list(CATEGORICAL_FEATURES | NUMERICAL_FEATURES)


class FeatureSelection(FeaturePreprocessor):
    @classmethod
    def extract_features_and_labels(cls, data: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame):
        features = data[cls.FEATURES]
        labels = data[[LABEL]]
        return features, labels


class FeatureEngineering(FeaturePreprocessor):
    def __init__(self, categorical_encoding: Literal["one_hot_encoding", "integer_encoding"]) -> None:
        self.categorical_encoding = categorical_encoding

    def transform(self, data: pd.DataFrame) -> None:
        data = data[self.FEATURES].copy()
        data = self._encode_categorical_features(data)
        return data

    def _encode_categorical_features(self, data: pd.DataFrame) -> pd.DataFrame:
        if self.categorical_encoding == "one_hot_encoding":
            return self._one_hot_encode_categorical_features(data)
        elif self.categorical_encoding == "integer_encoding":
            return self._integer_encode_categorical_features(data)

    def _one_hot_encode_categorical_features(self, data: pd.DataFrame) -> pd.DataFrame:
        return pd.get_dummies(data, columns=self.CATEGORICAL_FEATURES)

    def _integer_encode_categorical_features(self, data: pd.DataFrame) -> pd.DataFrame:
        for feature in self.CATEGORICAL_FEATURES:
            data[feature] = data[feature].astype("category").cat.codes
        return data
