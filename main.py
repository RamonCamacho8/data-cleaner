from src.loaders.loader_factory import LoaderFactory
from src.loaders.data_loader import DataLoader
from src.preprocessor.data_preprocessor import DataPreprocessor

import pandas as pd


def main(data_path: str):
    loader: DataLoader = LoaderFactory.get_loader("local", data_path)
    print("Hello from data-cleaner!")

    df: pd.DataFrame = loader.load_data(data_path)

    data, mappings = DataPreprocessor.clean_columns(df)

    data = DataPreprocessor.add_null_flags(
        data, target_cols=['score', 'es_fraude', 'monto', 'fech_registro'])

    DataPreprocessor.analyze_quality(data, target_col='monto', threshold=0.05)


if __name__ == "__main__":
    data_path: str = ".\\data\\dataset_sucio_ventas.csv"
    main(data_path)
