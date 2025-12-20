import pytest
import pandas as pd
from src.loaders.loader_factory import LoaderFactory


@pytest.fixture
def sample_csv_file(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    p = d / "test_data.csv"
    content = "Col 1, Col 2, Col 3\n1, 2, 3\n4, 5, 6"
    p.write_text(content, encoding='utf-8')
    return str(p)


def test_load_data_integration(sample_csv_file):

    loader = LoaderFactory.get_loader("local", sample_csv_file)
    df = loader.load_data(sample_csv_file)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df) == 2
    expected_columns = ["Col 1", " Col 2", " Col 3"]
    assert list(df.columns) == expected_columns
