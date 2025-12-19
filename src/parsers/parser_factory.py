from src.parsers.csv_parser import CSVParser

import os


class ParserFactory:

    @staticmethod
    def get_parser(file_path: str):

        file_type = ParserFactory._get_file_type(file_path)

        if file_type == 'csv':
            return CSVParser()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    @staticmethod
    def _get_file_type(file_path: str) -> str:
        _, extension = os.path.splitext(file_path)
        return extension.lstrip('.').lower()
