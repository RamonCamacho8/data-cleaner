from src.parsers.data_parser import DataParser

from abc import ABC, abstractmethod
import pandas as pd


class DataLoader(ABC):
    def __init__(self, parser: DataParser):
        self.parser = parser

    @abstractmethod
    def _fetch_content(self, path_or_key: str) -> str:
        pass

    def load_data(self, path_or_key: str) -> pd.DataFrame:
        """
        Ahora garantizamos que este método siempre devuelve un DataFrame.
        """
        raw_content = self._fetch_content(path_or_key)

        if not raw_content:
            return pd.DataFrame()

        return self.parser.parse(raw_content)
