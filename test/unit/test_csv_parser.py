import pytest
import pandas as pd
from src.parsers.csv_parser import CSVParser


class TestCSVParser:

    @pytest.fixture
    def parser(self):
        return CSVParser()

    @pytest.mark.parametrize("raw_content, expected_columns, expected_shape", [
        ("col1,col2\n1,2\n3,4", ["col1", "col2"], (2, 2)),
        ("a,b,c\n1,2,3", ["a", "b", "c"], (1, 3)),
        ("single_col\nval1\nval2", ["single_col"], (2, 1))
    ])
    def test_parse_success(self, parser, raw_content,
                           expected_columns, expected_shape):
        df = parser.parse(raw_content)

        assert isinstance(df, pd.DataFrame)
        assert df.shape == expected_shape
        assert list(df.columns) == expected_columns

    def test_parse_empty_string(self, parser):
        with pytest.raises(pd.errors.EmptyDataError):
            parser.parse("")
