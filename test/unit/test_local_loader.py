from src.loaders.local_loader import LocalLoader
from src.parsers.data_parser import DataParser

import pytest


class TestLocalLoader:

    @pytest.fixture
    def loader(self):
        class DummyParser(DataParser):
            def parse(self, raw_content: str):
                pass

        return LocalLoader(parser=DummyParser())

    @pytest.mark.parametrize("content, filename", [
        ("header1,header2\nval1,val2", "test1.csv"),
        ("simple content", "test2.txt"),
        ("", "empty.txt")
    ])
    def test_fetch_content_success(self, loader, tmp_path, content, filename):
        # Create a temporary file
        p = tmp_path / filename
        p.write_text(content, encoding='utf-8')

        # Test _fetch_content
        result = loader._fetch_content(str(p))
        assert result == content

    def test_fetch_content_file_not_found(self, loader):
        with pytest.raises(FileNotFoundError):
            loader._fetch_content("non_existent_file.txt")
