"""Unit tests for CogniStream feature engineering."""

import unittest

import pandas as pd


def add_features(df):
    """Create analytical features from developer activity data."""
    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["activity_date"] = df["timestamp"].dt.date

    df["total_disruptions"] = (
        df["interruption_count"] + df["context_switches"]
    )

    df["focus_category"] = pd.cut(
        df["focus_score"],
        bins=[-1, 59, 79, 100],
        labels=["Low", "Moderate", "High"],
    )

    df["workload_category"] = pd.cut(
        df["cognitive_load_score"],
        bins=[-1, 39, 69, 100],
        labels=[
            "Lower Indicator",
            "Moderate Indicator",
            "Higher Indicator",
        ],
    )

    return df


class TestFeatureEngineering(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
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
            "focus_score": [78, 88, 50],
            "cognitive_load_score": [35, 42, 75],
        })

        self.result = add_features(self.data)

    def test_hour_is_created(self):
        self.assertEqual(
            self.result["hour"].tolist(),
            [9, 10, 11],
        )

    def test_total_disruptions_is_calculated(self):
        self.assertEqual(
            self.result["total_disruptions"].tolist(),
            [3, 1, 8],
        )

    def test_focus_categories_are_correct(self):
        self.assertEqual(
            self.result["focus_category"].astype(str).tolist(),
            ["Moderate", "High", "Low"],
        )

    def test_workload_categories_are_correct(self):
        self.assertEqual(
            self.result["workload_category"].astype(str).tolist(),
            [
                "Lower Indicator",
                "Moderate Indicator",
                "Higher Indicator",
            ],
        )

    def test_activity_date_is_created(self):
        self.assertEqual(
            str(self.result.loc[0, "activity_date"]),
            "2026-10-20",
        )

    def test_original_dataframe_is_unchanged(self):
        self.assertNotIn("hour", self.data.columns)
        self.assertNotIn("focus_category", self.data.columns)


if __name__ == "__main__":
    unittest.main()
