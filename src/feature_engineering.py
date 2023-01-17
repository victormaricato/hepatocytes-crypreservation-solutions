from typing import Literal

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.base import TransformerMixin

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

    def fit(self, data: pd.DataFrame) -> None:
        if self.categorical_encoding == "one_hot_encoding":
            self._fit_one_hot_encoder(data)
        elif self.categorical_encoding == "integer_encoding":
            self._fit_integer_encoder(data)
        return self

    def _fit_one_hot_encoder(self, data: pd.DataFrame):
        self.encoder = OneHotEncoder()
        features = list(self.CATEGORICAL_FEATURES)
        self.encoder.fit(data[features])

    def _fit_integer_encoder(self, data: pd.DataFrame):
        self.integer_encoders = []

        for feature in self.CATEGORICAL_FEATURES:
            encoder = LabelEncoder()
            encoder.fit(data[feature])
            self.integer_encoders.append(encoder)

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
        features = list(self.CATEGORICAL_FEATURES)
        encoded_categorical_features = pd.DataFrame(self.encoder.transform(data[features]).toarray())
        encoded_categorical_features.columns = self.encoder.get_feature_names_out(features)
        data = pd.concat([data, encoded_categorical_features], axis=1)
        data = data.drop(self.CATEGORICAL_FEATURES, axis=1)
        return data

    def _integer_encode_categorical_features(self, data: pd.DataFrame) -> pd.DataFrame:
        features = list(self.CATEGORICAL_FEATURES)
        for feature, encoder in zip(features, self.integer_encoders):
            data[feature] = encoder.transform(data[feature])
        return data