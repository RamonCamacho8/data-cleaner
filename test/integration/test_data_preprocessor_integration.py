import pandas as pd
from src.preprocessor.data_preprocessor import DataPreprocessor


def test_clean_columns_integration():

    df = pd.DataFrame(
        [[1, 2, 3]],
        columns=["Col 1!", "Col 1@", "Col 2#"]
    )

    cleaned_df, mapping = DataPreprocessor.clean_columns(df)

    assert len(cleaned_df.columns) == 3
    assert len(set(cleaned_df.columns)) == 3

    expected_columns = ["col_1", "col_2", "col_3"]
    assert list(cleaned_df.columns) == expected_columns

    assert mapping["Col 1!"] == "col_1"
    assert mapping["Col 1@"] == "col_2"
    assert mapping["Col 2#"] == "col_3"
