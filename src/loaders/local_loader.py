from src.loaders.data_loader import DataLoader
import os


class LocalLoader(DataLoader):
    def _fetch_content(self, path_or_key: str) -> str:
        if not os.path.exists(path_or_key):
            raise FileNotFoundError(f"Archivo no encontrado: {path_or_key}")
        with open(path_or_key, 'r', encoding='utf-8') as file:
            return file.read()
