import pandas as pd

from src.constants import ESSAYS_DIR, ESSAYS


class Data:
    @staticmethod
    def load() -> pd.DataFrame:
        data = pd.DataFrame()
        for essay in ESSAYS:
            essay_data = pd.read_csv(ESSAYS_DIR + essay)
            data = pd.concat([data, essay_data])
        return data
