from src.loaders.data_loader import DataLoader
from src.loaders.local_loader import LocalLoader
from src.parsers.parser_factory import ParserFactory
from src.parsers.data_parser import DataParser


class LoaderFactory:
    @staticmethod
    def get_loader(source_type: str, file_path: str) -> DataLoader:

        parser: DataParser = ParserFactory.get_parser(file_path)

        if source_type == 'local':
            return LocalLoader(parser)
        else:
            raise ValueError(f"Fuente desconocida: {source_type}")
