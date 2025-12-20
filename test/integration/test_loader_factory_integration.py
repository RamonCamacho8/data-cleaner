import pytest
from src.loaders.loader_factory import LoaderFactory
from src.loaders.local_loader import LocalLoader
from src.parsers.csv_parser import CSVParser


@pytest.fixture
def sample_csv_file(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    p = d / "test_data.csv"
    content = "Col 1, Col 2, Col 3\n1, 2, 3\n4, 5, 6"
    p.write_text(content, encoding='utf-8')
    return str(p)


def test_get_loader_integration(sample_csv_file):

    loader = LoaderFactory.get_loader("local", sample_csv_file)
    assert isinstance(loader, LocalLoader)
    assert isinstance(loader.parser, CSVParser)
