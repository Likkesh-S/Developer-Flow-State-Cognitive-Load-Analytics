"""Generate a CogniStream exploratory data analysis report."""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "developer_activity.csv"
REPORT_DIR = PROJECT_ROOT / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)


def generate_report():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)
    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce"
    )

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
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    df = df.dropna(subset=required_columns).copy()
    df = df.sort_values("timestamp")

    # 1. Generate dataset overview.
    overview = pd.DataFrame({
        "Metric": [
            "Total records",
            "Number of developers",
            "Average coding minutes",
            "Average interruptions",
            "Average context switches",
            "Average focus score",
            "Average cognitive-load indicator",
        ],
        "Value": [
            len(df),
            df["developer_id"].nunique(),
            round(df["coding_minutes"].mean(), 2),
            round(df["interruption_count"].mean(), 2),
            round(df["context_switches"].mean(), 2),
            round(df["focus_score"].mean(), 2),
            round(df["cognitive_load_score"].mean(), 2),
        ],
    })

    overview.to_csv(
        REPORT_DIR / "eda_overview.csv",
        index=False,
    )

    # 2. Generate descriptive statistics.
    numeric_columns = [
        "coding_minutes",
        "interruption_count",
        "context_switches",
        "task_complexity",
        "break_minutes",
        "focus_score",
        "cognitive_load_score",
    ]

    df[numeric_columns].describe().round(2).to_csv(
        REPORT_DIR / "descriptive_statistics.csv"
    )

    # 3. Developer-level summary.
    developer_summary = (
        df.groupby("developer_id")
        .agg(
            activity_records=("timestamp", "count"),
            total_coding_minutes=("coding_minutes", "sum"),
            average_focus=("focus_score", "mean"),
            total_interruptions=("interruption_count", "sum"),
            total_context_switches=("context_switches", "sum"),
            average_cognitive_load=(
                "cognitive_load_score", "mean"
            ),
        )
        .round(2)
        .reset_index()
    )

    developer_summary.to_csv(
        REPORT_DIR / "developer_summary.csv",
        index=False,
    )

    # 4. Plot average focus by developer.
    plt.figure(figsize=(8, 5))
    focus_by_developer = df.groupby(
        "developer_id"
    )["focus_score"].mean()

    focus_by_developer.plot(kind="bar")
    plt.title("Average Simulated Focus Score by Developer")
    plt.xlabel("Developer")
    plt.ylabel("Average Focus Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "focus_by_developer.png")
    plt.close()

    # 5. Plot interruptions against focus.
    plt.figure(figsize=(8, 5))
    plt.scatter(
        df["interruption_count"],
        df["focus_score"],
    )
    plt.title("Interruptions vs Simulated Focus Score")
    plt.xlabel("Interruption Count")
    plt.ylabel("Focus Score")
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "interruptions_vs_focus.png")
    plt.close()

    # 6. Plot the cognitive-load indicator distribution.
    plt.figure(figsize=(8, 5))
    df["cognitive_load_score"].plot(
        kind="hist", bins=10
    )
    plt.title("Distribution of Cognitive-Load Indicators")
    plt.xlabel("Cognitive-Load Indicator")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "cognitive_load_distribution.png")
    plt.close()

    # 7. Calculate correlation for exploratory purposes.
    correlation = df[
        ["interruption_count", "context_switches",
         "focus_score", "cognitive_load_score"]
    ].corr().round(3)

    correlation.to_csv(
        REPORT_DIR / "correlation_matrix.csv"
    )

    print("CogniStream EDA report generated successfully.")
    print(f"Records analyzed: {len(df)}")
    print(f"Developers analyzed: {df['developer_id'].nunique()}")
    print(f"Report folder: {REPORT_DIR}")
    print("\nDataset overview:")
    print(overview.to_string(index=False))
    print("\nDeveloper summary:")
    print(developer_summary.to_string(index=False))


if __name__ == "__main__":
    generate_report()
