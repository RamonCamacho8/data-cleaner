import pytest
from src.parsers.parser_factory import ParserFactory
from src.parsers.csv_parser import CSVParser


@pytest.fixture
def sample_csv_file(tmp_path):
    """Creates a temporary CSV file for testing."""
    d = tmp_path / "data"
    d.mkdir()
    p = d / "test_data.csv"
    content = "Col 1, Col 2, Col 3\n1, 2, 3\n4, 5, 6"
    p.write_text(content, encoding='utf-8')
    return str(p)


def test_get_parser_integration(sample_csv_file):
    """
    Test that ParserFactory correctly identifies and returns a CSVParser
    for a .csv file.
    """
    parser = ParserFactory.get_parser(sample_csv_file)
    assert isinstance(parser, CSVParser)
