from src.parsers.data_parser import DataParser
import pandas as pd
from io import StringIO


class CSVParser(DataParser):
    def parse(self, raw_content: str) -> pd.DataFrame:
        return pd.read_csv(StringIO(raw_content))
