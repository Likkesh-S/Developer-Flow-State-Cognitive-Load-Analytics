from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_cleaned.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_features.csv"
)


def create_features(input_file=INPUT_FILE):
    """Create analytical features from cleaned activity data."""

    df = pd.read_csv(input_file, parse_dates=["timestamp"])

    required_columns = [
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

    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    # Calendar features
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["activity_date"] = df["timestamp"].dt.date

    # Combined interruption and context-switching indicator
    df["total_disruptions"] = (
        df["interruption_count"] + df["context_switches"]
    )

    # Simple descriptive categories
    df["focus_category"] = pd.cut(
        df["focus_score"],
        bins=[-1, 59, 79, 100],
        labels=["Low Focus", "Moderate Focus", "High Focus"],
    )

    df["workload_category"] = pd.cut(
        df["cognitive_load_score"],
        bins=[-1, 39, 69, 100],
        labels=["Lower Indicator", "Moderate Indicator", "Higher Indicator"],
    )

    # Daily summaries for each developer
    daily_summary = (
        df.groupby(["developer_id", "activity_date"], as_index=False)
        .agg(
            total_coding_minutes=("coding_minutes", "sum"),
            total_interruptions=("interruption_count", "sum"),
            total_context_switches=("context_switches", "sum"),
            average_focus_score=("focus_score", "mean"),
            average_cognitive_load=("cognitive_load_score", "mean"),
            activity_records=("timestamp", "count"),
        )
    )

    # Save record-level features and daily summary
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    summary_file = OUTPUT_FILE.parent / "daily_developer_summary.csv"
    daily_summary.to_csv(summary_file, index=False)

    print("Feature engineering completed.")
    print(f"Feature dataset: {OUTPUT_FILE}")
    print(f"Daily summary: {summary_file}")

    print("\nFeature dataset preview:")
    print(df.head())

    print("\nDaily developer summary:")
    print(daily_summary.head())

    return df, daily_summary


if __name__ == "__main__":
    create_features()
