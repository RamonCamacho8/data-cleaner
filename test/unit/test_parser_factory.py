from src.parsers.parser_factory import ParserFactory


import pytest


class TestParserFactory:

    @pytest.mark.parametrize("file_path, expected_type", [
        ("data.csv", "csv"),
        ("path/to/file.json", "json"),
        ("MYFILE.TXT", "txt"),
        ("archive.tar.gz", "gz"),
        (".gitignore", ""),
        ("script.py", "py")
    ])
    def test_get_file_type(self, file_path, expected_type):
        assert ParserFactory._get_file_type(file_path) == expected_type

    @pytest.mark.parametrize("file_path", [
        "file_no_extension",
        "path/to/file"
    ])
    def test_get_file_type_no_extension(self, file_path):
        assert ParserFactory._get_file_type(file_path) == ""
