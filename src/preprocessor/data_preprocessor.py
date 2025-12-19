import pandas as pd
import re
from collections import Counter
from typing import Tuple, Dict


class DataPreprocessor:

    @staticmethod
    def _remove_special_chars(text: str) -> str:
        """
        Removes special characters from a string.

        Args:
            text (str): The input string.
        Returns:
            str: The cleaned string.
        """
        return re.sub(r'[^\w\s]', '', text)

    @staticmethod
    def _remove_digits(text: str) -> str:
        """
        Removes all digits (0-9) from a string.

        Args:
            text (str): The input string.
        Returns:
            str: The string with digits removed.
        """
        return re.sub(r'\d+', '', text)

    @staticmethod
    def _replace_spaces(text: str, replacement: str = '_') -> str:
        """
        Replaces spaces in a string with a specified replacement character.

        Args:
            text (str): The input string.
            replacement (str): The character to replace spaces with.
        Returns:
            str: The modified string.
        """
        return re.sub(r'\s+', replacement, text)

    @staticmethod
    def _to_lowercase(text: str) -> str:
        """
        Converts all characters in a string to lowercase.

        Args:
            text (str): The input string.
        Returns:
            str: The lowercase string.
        """
        return text.lower()

    @staticmethod
    def _strip_residues(text: str) -> str:
        """
        Strips leading and trailing underscores from a string.
        Args:
            text (str): The input string.
        Returns:
            str: The stripped string.
        """
        return text.strip('_')

    @staticmethod
    def _consolidate_underscores(text: str) -> str:
        """
        Consolidates multiple consecutive underscores into a single underscore.
        Args:
            text (str): The input string.
        Returns:
            str: The modified string.
        """
        return re.sub(r'_{2,}', '_', text)

    @staticmethod
    def _handle_duplicates(columns: list[str]) -> list[str]:
        """
        Search for duplicate column names and append
        a suffix to make them unique.

        Args:
            columns (list[str]): List of column names.
        Returns:
            list[str]: List of unique column names.
        """
        counts = Counter(columns)

        seen_counter = {}
        final_columns = []

        for col in columns:
            if counts[col] > 1:
                seen_counter[col] = seen_counter.get(col, 0) + 1
                new_name = f"{col}_{seen_counter[col]}"
                final_columns.append(new_name)
            else:
                final_columns.append(col)

        return final_columns

    @staticmethod
    def _columns_mapping(
            original: list[str], cleaned: list[str]
    ) -> Dict[str, str]:

        """
        Creates a mapping from original column names to cleaned column names.
        Args:
            original (list[str]): List of original column names.
            cleaned (list[str]): List of cleaned column names.
        Returns:
            Dict[str, str]: A dict mapping original names to cleaned names.
        """
        return dict(zip(original, cleaned))

    @staticmethod
    def clean_columns(
        dataframe: pd.DataFrame,
    ) -> Tuple[pd.DataFrame, Dict[str, str]]:
        """
        Clean column names of a DataFrame by applying
        a series of transformations:
        - Remove special characters
        - Remove digits
        - Convert to lowercase
        - Replace spaces with underscores
        - Consolidate multiple underscores
        - Strip leading/trailing underscores

        Also handles duplicate column names by appending
        a sequential suffix.

        Returns the cleaned DataFrame and a mapping of original
        to cleaned column names.


        Args:
            dataframe (pd.DataFrame): The DataFrame to clean.
        Returns:
            Tuple[pd.DataFrame, Dict[str, str]]: A tuple containing
            the cleaned DataFrame and a dictionary mapping original
            column names to cleaned column names.

        """

        df = dataframe.copy()

        temp_columns = []

        for col in df.columns:
            clean_col = col
            clean_col = DataPreprocessor._remove_special_chars(clean_col)
            clean_col = DataPreprocessor._remove_digits(clean_col)
            clean_col = DataPreprocessor._to_lowercase(clean_col)
            clean_col = DataPreprocessor._replace_spaces(clean_col)
            clean_col = DataPreprocessor._consolidate_underscores(clean_col)
            clean_col = DataPreprocessor._strip_residues(clean_col)

            temp_columns.append(clean_col)

        final_columns = DataPreprocessor._handle_duplicates(temp_columns)
        df.columns = final_columns
        mapping = DataPreprocessor._columns_mapping(
            dataframe.columns.tolist(), final_columns
        )

        return df, mapping

    def add_null_flags(self):
        pass

    def analyze_quality(self):
        pass
