"""Unit tests for CogniStream data cleaning."""

import tempfile
import unittest
from pathlib import Path

import pandas as pd

from src.data_cleaning import clean_developer_data


class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        """Create a temporary CSV for each test."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.input_file = Path(self.temp_dir.name) / "input.csv"

        self.valid_data = pd.DataFrame({
            "timestamp": [
                "2026-10-20 09:00:00",
                "2026-10-20 10:00:00",
                "2026-10-20 11:00:00",
            ],
            "developer_id": ["DEV001", "DEV001", "DEV002"],
            "coding_minutes": [42, 50, 35],
            "interruption_count": [1, 0, 3],
            "context_switches": [2, 1, 5],
            "task_complexity": [3, 4, 4],
            "break_minutes": [5, 5, 10],
            "focus_score": [78, 88, 61],
            "cognitive_load_score": [35, 42, 68],
        })

        self.valid_data.to_csv(self.input_file, index=False)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_valid_records_are_loaded(self):
        """Valid records should remain after cleaning."""
        cleaned = clean_developer_data(self.input_file)

        self.assertEqual(len(cleaned), 3)
        self.assertIn("developer_id", cleaned.columns)

    def test_duplicate_records_are_removed(self):
        """Duplicate complete rows should be removed."""
        duplicate_data = pd.concat(
            [self.valid_data, self.valid_data.iloc[[0]]],
            ignore_index=True,
        )
        duplicate_data.to_csv(self.input_file, index=False)

        cleaned = clean_developer_data(self.input_file)

        self.assertEqual(len(cleaned), 3)

    def test_invalid_focus_score_is_removed(self):
        """Focus scores outside 0-100 should be removed."""
        invalid_data = self.valid_data.copy()
        invalid_data.loc[0, "focus_score"] = 120
        invalid_data.to_csv(self.input_file, index=False)

        cleaned = clean_developer_data(self.input_file)

        self.assertEqual(len(cleaned), 2)

    def test_invalid_task_complexity_is_removed(self):
        """Task complexity must be between 1 and 5."""
        invalid_data = self.valid_data.copy()
        invalid_data.loc[0, "task_complexity"] = 8
        invalid_data.to_csv(self.input_file, index=False)

        cleaned = clean_developer_data(self.input_file)

        self.assertEqual(len(cleaned), 2)

    def test_missing_required_column_raises_error(self):
        """A missing required column should raise ValueError."""
        invalid_data = self.valid_data.drop(columns=["focus_score"])
        invalid_data.to_csv(self.input_file, index=False)

        with self.assertRaises(ValueError):
            clean_developer_data(self.input_file)


if __name__ == "__main__":
    unittest.main()
