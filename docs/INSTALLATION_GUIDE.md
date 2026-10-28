# CogniStream - Installation Guide

## 1. Project Overview

CogniStream is a developer activity analytics project that uses Python, SQL, machine learning, and Streamlit to analyze simulated developer activity.

The project explores coding time, interruptions, context switching, focus scores, and cognitive-load indicators.

**Important:** The dataset is simulated. Focus and cognitive-load scores are illustrative indicators, not clinical measurements or validated psychological assessments.

## 2. System Requirements

- Windows 10 or Windows 11
- Python 3.10 or newer
- GitHub project downloaded to your computer
- Internet connection for installing Python packages
- A code editor such as Visual Studio Code (optional)

## 3. Download the Project

1. Open the CogniStream GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file.
5. Open the extracted `cognistream-developer-analytics` folder.

Make sure the project folders, including `data`, `src`, `sql`, `tests`, and `docs`, are present.

## 4. Verify Python Installation

Open the project folder in File Explorer.

Click the address bar, type `cmd`, and press Enter.

Run:

```bash
python --version
```

If that command does not work, try:

```bash
py --version
```

If Python is not installed, install it from:

https://www.python.org/downloads/

During installation, select **Add Python to PATH** if that option is available.

## 5. Create a Virtual Environment (Recommended)

Run these commands in the project folder:

```bash
python -m venv .venv
```

Activate the environment:

```bash
.venv\Scripts\activate
```

If the `python` command is unavailable but `py` works, use `py` in the commands instead.

## 6. Install Required Libraries

Run:

```bash
python -m pip install --upgrade pip
```

Then install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Wait until the installation finishes.

## 7. Run the Project Pipeline

Run the following commands from the repository's root folder, in order.

### Step 1: Clean the Dataset

```bash
python src/data_cleaning.py
```

This checks the input data and creates the cleaned dataset under `data/processed/`.

### Step 2: Generate Features

```bash
python src/feature_engineering.py
```

This creates additional time-based features, categories, and a daily developer summary.

### Step 3: Load Data into SQLite

```bash
python src/load_data_to_sqlite.py
```

This creates or updates the SQLite database at `data/cognistream.db`.

**Note:** Running this loader again replaces the existing rows in the database table.

### Step 4: Generate Exploratory Data Analysis Reports

```bash
python src/eda_report.py
```

This generates summary CSV files and charts in the `reports/` folder.

### Step 5: Train the Demonstration Model

```bash
python src/model_training.py
```

This trains a sample machine-learning classifier and saves the model and evaluation information in `models/`.

The results are for demonstration only because the dataset is small and simulated.

## 8. Launch the Dashboard

Run:

```bash
python -m streamlit run app.py
```

Streamlit should open the application in your web browser.

If the home-page navigation does not open the dashboard, run the dashboard directly:

```bash
python -m streamlit run src/visualize_dashboard.py
```

To stop the application, return to Command Prompt and press `Ctrl + C`.

## 9. Run the Tests

Run:

```bash
python -m unittest discover -s tests -v
```

Review the output to see which tests passed or failed.

If a test cannot import a module from `src`, create an empty file named `src/__init__.py` and run the tests again.

## 10. Expected Project Outputs

After running the pipeline successfully, the project may contain:

- `data/processed/developer_activity_cleaned.csv`
- `data/processed/developer_activity_features.csv`
- `data/processed/daily_developer_summary.csv`
- `data/cognistream.db`
- `reports/eda_overview.csv`
- `reports/descriptive_statistics.csv`
- `reports/developer_summary.csv`
- `reports/correlation_matrix.csv`
- `reports/focus_by_developer.png`
- `reports/interruptions_vs_focus.png`
- `reports/cognitive_load_distribution.png`
- `models/focus_classifier.joblib`
- `models/model_metrics.txt`

Generated files appear only after their corresponding scripts run successfully.

## 11. Common Problems and Solutions

### Python is not recognized

Try `py --version`. If Python is missing, install it and reopen Command Prompt.

### Requirements installation fails

Check your internet connection and run:

```bash
python -m pip install -r requirements.txt
```

### Dataset file not found

Check that `data/developer_activity.csv` exists and that Command Prompt is open in the repository root folder.

### Streamlit command is not recognized

Run:

```bash
python -m pip install streamlit
python -m streamlit run app.py
```

### Processed data file is missing

Run the data-cleaning script first, followed by feature engineering.

### Model training fails

Confirm that the feature-engineering script completed successfully and created `data/processed/developer_activity_features.csv`.

## 12. Conclusion

This guide provides the steps to install, execute, test, and explore the CogniStream project on Windows.

The project demonstrates a basic analytics workflow involving data preparation, feature engineering, SQL storage, exploratory analysis, machine learning, and dashboard visualization.
