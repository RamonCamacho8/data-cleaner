from abc import ABC, abstractmethod
import pandas as pd


class DataParser(ABC):

    @abstractmethod
    def parse(self, raw_content: str) -> pd.DataFrame:
        pass
