"""Unit tests for CogniStream SQL database operations."""

import sqlite3
import tempfile
import unittest
from pathlib import Path


class TestSQLQueries(unittest.TestCase):

    def setUp(self):
        # Create a temporary database for each test.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test.db"

        with sqlite3.connect(self.db_path) as connection:
            connection.executescript("""
                CREATE TABLE developer_activity (
                    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    developer_id TEXT NOT NULL,
                    coding_minutes INTEGER NOT NULL
                        CHECK (coding_minutes >= 0),
                    interruption_count INTEGER NOT NULL
                        CHECK (interruption_count >= 0),
                    context_switches INTEGER NOT NULL
                        CHECK (context_switches >= 0),
                    task_complexity INTEGER NOT NULL
                        CHECK (task_complexity BETWEEN 1 AND 5),
                    break_minutes INTEGER NOT NULL
                        CHECK (break_minutes >= 0),
                    focus_score REAL NOT NULL
                        CHECK (focus_score BETWEEN 0 AND 100),
                    cognitive_load_score REAL NOT NULL
                        CHECK (cognitive_load_score BETWEEN 0 AND 100)
                );

                INSERT INTO developer_activity (
                    timestamp, developer_id, coding_minutes,
                    interruption_count, context_switches,
                    task_complexity, break_minutes,
                    focus_score, cognitive_load_score
                ) VALUES
                    ('2026-10-20 09:00:00', 'DEV001',
                     42, 1, 2, 3, 5, 78, 35),
                    ('2026-10-20 10:00:00', 'DEV001',
                     50, 0, 1, 4, 5, 88, 42),
                    ('2026-10-20 11:00:00', 'DEV002',
                     35, 3, 5, 4, 10, 61, 68);
            """)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_table_contains_three_records(self):
        with sqlite3.connect(self.db_path) as connection:
            count = connection.execute(
                "SELECT COUNT(*) FROM developer_activity"
            ).fetchone()[0]

        self.assertEqual(count, 3)

    def test_total_coding_minutes_by_developer(self):
        with sqlite3.connect(self.db_path) as connection:
            result = connection.execute("""
                SELECT developer_id, SUM(coding_minutes)
                FROM developer_activity
                GROUP BY developer_id
                ORDER BY developer_id
            """).fetchall()

        self.assertEqual(
            result,
            [("DEV001", 92), ("DEV002", 35)],
        )

    def test_average_focus_score(self):
        with sqlite3.connect(self.db_path) as connection:
            result = connection.execute("""
                SELECT ROUND(AVG(focus_score), 2)
                FROM developer_activity
                WHERE developer_id = 'DEV001'
            """).fetchone()[0]

        self.assertEqual(result, 83.0)

    def test_invalid_focus_score_is_rejected(self):
        with sqlite3.connect(self.db_path) as connection:
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute("""
                    INSERT INTO developer_activity (
                        timestamp, developer_id, coding_minutes,
                        interruption_count, context_switches,
                        task_complexity, break_minutes,
                        focus_score, cognitive_load_score
                    ) VALUES (
                        '2026-10-20 12:00:00', 'DEV003',
                        20, 0, 0, 3, 5, 120, 40
                    )
                """)

    def test_daily_summary_query(self):
        with sqlite3.connect(self.db_path) as connection:
            result = connection.execute("""
                SELECT
                    developer_id,
                    DATE(timestamp),
                    SUM(coding_minutes)
                FROM developer_activity
                GROUP BY developer_id, DATE(timestamp)
                ORDER BY developer_id
            """).fetchall()

        self.assertEqual(
            result,
            [
                ("DEV001", "2026-10-20", 92),
                ("DEV002", "2026-10-20", 35),
            ],
        )


if __name__ == "__main__":
    unittest.main()
