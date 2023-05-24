"""

"""
from abc import ABC, abstractmethod

import pandas as pd


class BaseReader(ABC):
    RAW_COLS: list[str] | list[tuple[str]] = []

    def __init__(self):
        self.df = self._get_raw_df()

    @abstractmethod
    def _get_raw_df(self) -> pd.DataFrame:
        raise NotImplementedError

    def _drop_names(self) -> None:
        print(self.df)
        pass
