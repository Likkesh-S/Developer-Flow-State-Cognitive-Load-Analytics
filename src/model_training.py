from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_features.csv"
)

MODEL_DIR = PROJECT_ROOT / "models"
MODEL_FILE = MODEL_DIR / "focus_classifier.joblib"
METRICS_FILE = MODEL_DIR / "model_metrics.txt"

FEATURES = [
    "coding_minutes",
    "interruption_count",
    "context_switches",
    "task_complexity",
    "break_minutes",
    "cognitive_load_score",
]

TARGET = "focus_category"


def train_model():
    """Train and evaluate an experimental focus-category classifier."""

    df = pd.read_csv(INPUT_FILE)

    # Create target labels using the project's predefined thresholds.
    # These labels are illustrative, not psychological assessments.
    df[TARGET] = pd.cut(
        df["focus_score"],
        bins=[-1, 59, 79, 100],
        labels=["Low Focus", "Moderate Focus", "High Focus"],
    )

    df = df.dropna(subset=[TARGET])

    X = df[FEATURES]
    y = df[TARGET].astype(str)

    if y.nunique() < 2:
        raise ValueError("At least two focus categories are required.")

    # Stratify only when every class has enough records.
    class_counts = y.value_counts()
    stratify_labels = (
        y if class_counts.min() >= 2 else None
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=stratify_labels,
    )

    model = make_pipeline(
        SimpleImputer(strategy="median"),
        RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight="balanced",
        ),
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    report = classification_report(
        y_test,
        predictions,
        zero_division=0,
    )

    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=["Low Focus", "Moderate Focus", "High Focus"],
    )

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_FILE)

    with open(METRICS_FILE, "w", encoding="utf-8") as file:
        file.write(f"Test accuracy: {accuracy:.3f}\n\n")
        file.write("Classification report:\n")
        file.write(report)
        file.write("\nConfusion matrix:\n")
        file.write(str(matrix))

    print("Model training completed.")
    print(f"Test accuracy: {accuracy:.3f}")
    print("\nClassification report:")
    print(report)
    print("\nConfusion matrix:")
    print(matrix)
    print(f"\nSaved model: {MODEL_FILE}")
    print(f"Saved metrics: {METRICS_FILE}")

    return model


if __name__ == "__main__":
    train_model()
