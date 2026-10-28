"""Load CogniStream CSV activity data into SQLite."""

import sqlite3
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_FILE = PROJECT_ROOT / "data" / "developer_activity.csv"
SQL_FILE = PROJECT_ROOT / "sql" / "create_tables.sql"
DATABASE_FILE = PROJECT_ROOT / "data" / "cognistream.db"

REQUIRED_COLUMNS = [
    "timestamp",
    "developer_id",
    "coding_minutes",
    "interruption_count",
    "context_switches",
    "task_complexity",
    "break_minutes",
    "focus_score",
    "cognitive_load_score",
]


def load_data():
    """Validate the CSV and load records into SQLite."""

    if not CSV_FILE.exists():
        raise FileNotFoundError(
            f"CSV file not found: {CSV_FILE}"
        )

    if not SQL_FILE.exists():
        raise FileNotFoundError(
            f"SQL schema not found: {SQL_FILE}"
        )

    df = pd.read_csv(CSV_FILE)

    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    df = df[REQUIRED_COLUMNS].copy()

    # Convert values to the expected data types.
    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce"
    )
    numeric_columns = [
        "coding_minutes",
        "interruption_count",
        "context_switches",
        "task_complexity",
        "break_minutes",
        "focus_score",
        "cognitive_load_score",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

    # Reject invalid or incomplete records.
    df = df.dropna(subset=REQUIRED_COLUMNS)
    df["developer_id"] = df["developer_id"].astype(str).str.strip()
    df = df[df["developer_id"] != ""]

    nonnegative_columns = [
        "coding_minutes",
        "interruption_count",
        "context_switches",
        "break_minutes",
    ]

    for column in nonnegative_columns:
        df = df[df[column] >= 0]

    df = df[df["task_complexity"].between(1, 5)]
    df = df[df["focus_score"].between(0, 100)]
    df = df[df["cognitive_load_score"].between(0, 100)]

    # SQLite table uses INTEGER for these columns.
    for column in [
        "coding_minutes",
        "interruption_count",
        "context_switches",
        "task_complexity",
        "break_minutes",
    ]:
        df = df[df[column] % 1 == 0]
        df[column] = df[column].astype(int)

    df = df.drop_duplicates(subset=REQUIRED_COLUMNS)

    # Create the database and table.
    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.executescript(
            SQL_FILE.read_text(encoding="utf-8")
        )

        # Replace previous imported records so rerunning
        # this script does not append duplicate imports.
        connection.execute("DELETE FROM developer_activity")

        df["timestamp"] = df["timestamp"].dt.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        df.to_sql(
            "developer_activity",
            connection,
            if_exists="append",
            index=False,
        )

        total = connection.execute(
            "SELECT COUNT(*) FROM developer_activity"
        ).fetchone()[0]

    print("CogniStream data import completed.")
    print(f"Valid records loaded: {total}")
    print(f"Database saved to: {DATABASE_FILE}")

    return total


if __name__ == "__main__":
    load_data()
