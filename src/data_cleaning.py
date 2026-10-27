from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "developer_activity.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "developer_activity_cleaned.csv"

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


def clean_developer_data(input_file=INPUT_FILE):
    """Load, validate, and clean simulated developer activity data."""

    # Load data and check required fields
    df = pd.read_csv(input_file)

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    df = df[REQUIRED_COLUMNS].copy()

    # Convert timestamp and numeric fields
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

    # Remove records without essential identifiers or timestamps
    df = df.dropna(subset=["timestamp", "developer_id"])
    df["developer_id"] = df["developer_id"].astype(str).str.strip()
    df = df[df["developer_id"] != ""]

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Validate allowed numeric ranges
    valid = (
        (df["coding_minutes"] >= 0)
        & (df["interruption_count"] >= 0)
        & (df["context_switches"] >= 0)
        & (df["break_minutes"] >= 0)
        & (df["task_complexity"].between(1, 5))
        & (df["focus_score"].between(0, 100))
        & (df["cognitive_load_score"].between(0, 100))
    )

    df = df.loc[valid].copy()

    # Handle remaining missing numeric values with column medians
    for column in numeric_columns:
        if df[column].isna().any():
            median_value = df[column].median()
            if pd.notna(median_value):
                df[column] = df[column].fillna(median_value)

    # Sort data consistently
    df = df.sort_values(
        ["developer_id", "timestamp"]
    ).reset_index(drop=True)

    # Save processed data
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("Data cleaning completed.")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Cleaned rows: {len(df)}")
    print(f"Remaining missing values: {df.isna().sum().sum()}")

    return df


if __name__ == "__main__":
    cleaned_df = clean_developer_data()
    print(cleaned_df.head())
