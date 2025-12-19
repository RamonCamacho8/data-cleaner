import pytest
import pandas as pd
from src.preprocessor.data_preprocessor import DataPreprocessor


class TestDataPreprocessor:

    @pytest.mark.parametrize("input_text, expected", [
        ("Hello, World!", "Hello World"),
        ("Python@3.9", "Python39"),
        ("NoSpecialChars", "NoSpecialChars"),
        ("!!!", "")
    ])
    def test_remove_special_chars(self, input_text, expected):
        assert DataPreprocessor._remove_special_chars(input_text) == expected

    @pytest.mark.parametrize("input_text, expected", [
        ("User123", "User"),
        ("2023Year", "Year"),
        ("NoDigits", "NoDigits"),
        ("123456", "")
    ])
    def test_remove_digits(self, input_text, expected):
        assert DataPreprocessor._remove_digits(input_text) == expected

    @pytest.mark.parametrize("input_text, replacement, expected", [
        ("Hello World", "_", "Hello_World"),
        ("  Multiple   Spaces  ", "-", "-Multiple-Spaces-"),
        ("NoSpaces", "_", "NoSpaces"),
        ("Tab\tSpace", "_", "Tab_Space")
    ])
    def test_replace_spaces(self, input_text, replacement, expected):
        assert DataPreprocessor._replace_spaces(
            input_text, replacement) == expected

    @pytest.mark.parametrize("input_text, expected", [
        ("Hello", "hello"),
        ("UPPERCASE", "uppercase"),
        ("MixedCase", "mixedcase"),
        ("123", "123")
    ])
    def test_to_lowercase(self, input_text, expected):
        assert DataPreprocessor._to_lowercase(input_text) == expected

    @pytest.mark.parametrize("input_text, expected", [
        ("_start", "start"),
        ("end_", "end"),
        ("_both_", "both"),
        ("__double__", "double"),
        ("none", "none")
    ])
    def test_strip_residues(self, input_text, expected):
        assert DataPreprocessor._strip_residues(input_text) == expected

    @pytest.mark.parametrize("input_text, expected", [
        ("one__two", "one_two"),
        ("three___four", "three_four"),
        ("five_six", "five_six"),
        ("seven____eight", "seven_eight")
    ])
    def test_consolidate_underscores(self, input_text, expected):
        assert DataPreprocessor._consolidate_underscores(
            input_text) == expected

    @pytest.mark.parametrize("columns, expected", [
        (["col", "col", "col"], ["col_1", "col_2", "col_3"]),
        (["a", "b", "c"], ["a", "b", "c"]),
        (["a", "b", "a"], ["a_1", "b", "a_2"]),
        ([], [])
    ])
    def test_handle_duplicates(self, columns, expected):
        assert DataPreprocessor._handle_duplicates(columns) == expected

    def test_columns_mapping(self):
        original = ["a", "b", "c"]
        cleaned = ["x", "y", "z"]
        expected = {"a": "x", "b": "y", "c": "z"}
        assert DataPreprocessor._columns_mapping(original, cleaned) == expected

    def test_add_null_flags(self):
        df = pd.DataFrame({
            "A": [1, None, 3],
            "B": [None, 5, 6],
            "C": [7, 8, 9]
        })
        target_cols = ["A", "B"]

        result_df = DataPreprocessor.add_null_flags(df, target_cols)

        assert "A_nan" in result_df.columns
        assert "B_nan" in result_df.columns
        assert "C_nan" not in result_df.columns

        assert result_df["A_nan"].tolist() == [0, 1, 0]
        assert result_df["B_nan"].tolist() == [1, 0, 0]

        assert result_df["A"].equals(df["A"])

    def test_analyze_quality_acceptable(self, capsys):
        df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5]
        })

        DataPreprocessor.analyze_quality(df, "A", threshold=0.05)

        captured = capsys.readouterr()
        assert "La calidad de los datos es aceptable." in captured.out
        assert "ALERTA" not in captured.out

    def test_analyze_quality_alert(self, capsys):
        df = pd.DataFrame({
            "A": [1, None, 3, 4, 5]
        })

        DataPreprocessor.analyze_quality(df, "A", threshold=0.05)

        captured = capsys.readouterr()
        assert "ALERTA: Esto excede el umbral" in captured.out
        assert "Se recomienda descartar el dataset" in captured.out
