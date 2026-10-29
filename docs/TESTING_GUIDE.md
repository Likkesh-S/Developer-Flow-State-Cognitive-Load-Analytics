# CogniStream - Testing Guide

## 1. Introduction

This document describes the testing procedures for the CogniStream project.

Testing helps verify that data cleaning, feature engineering, SQL operations, model training, and dashboard components work as expected.

The project uses Python's built-in `unittest` framework for automated tests.

## 2. Testing Objectives

The main objectives are:

- Verify that input data is validated correctly.
- Check that duplicate and invalid records are handled.
- Confirm that derived features are generated.
- Validate SQL query results.
- Check that model training produces the expected output files.
- Confirm that the dashboard starts successfully.
- Identify errors before project submission.

## 3. Prerequisites

Before testing, confirm that:

- Python is installed.
- The project repository is downloaded.
- Required dependencies are installed.
- The original dataset exists at `data/developer_activity.csv`.
- The terminal is open in the repository's root directory.

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

## 4. Run the Automated Tests

Execute the following command from the repository root:

```bash
python -m unittest discover -s tests -v
```

This command discovers test files in the `tests/` directory and displays individual test results.

If the project uses a virtual environment, activate it before running the command.

## 5. Data Cleaning Tests

### Test File

`tests/test_data_cleaning.py`

### What It Checks

- Valid records are retained.
- Duplicate records are removed.
- Invalid focus scores are rejected.
- Invalid task complexity values are rejected.
- Missing required columns raise an error.

### Run

```bash
python -m unittest tests.test_data_cleaning -v
```

If the module cannot be imported, use the general test-discovery command in Section 4.

### Expected Result

Each test should report `ok` when its assertion passes. A failing test should be investigated before marking the test as successful.

## 6. Feature Engineering Tests

### Test File

`tests/test_feature_engineering.py`

### What It Checks

- Hour is extracted from the timestamp.
- Day of the week is generated.
- Activity date is generated.
- Total disruptions are calculated.
- Focus categories are assigned.
- Workload categories are assigned.

### Run

```bash
python -m unittest tests.test_feature_engineering -v
```

### Expected Result

The tests should confirm that the expected derived columns exist and that their values match the test examples.

## 7. SQL Tests

### Test File

`tests/test_sql_queries.py`

### What It Checks

- Records can be inserted into a temporary SQLite database.
- Coding-time totals are calculated correctly.
- Average focus scores are calculated correctly.
- Invalid score values are rejected by the test schema.
- Daily summaries return expected totals.

### Run

```bash
python -m unittest tests.test_sql_queries -v
```

### Expected Result

The assertions should pass for the test records defined in the test file.

These tests use a temporary database and do not by themselves prove that every production SQL query is correct.

## 8. Data Pipeline Validation

Run the processing scripts in the following order.

### Step 1: Clean the Data

```bash
python src/data_cleaning.py
```

Check that:

`data/processed/developer_activity_cleaned.csv`

is created.

### Step 2: Generate Features

```bash
python src/feature_engineering.py
```

Check for:

- `data/processed/developer_activity_features.csv`
- `data/processed/daily_developer_summary.csv`

### Step 3: Load the Database

```bash
python src/load_data_to_sqlite.py
```

Check that:

`data/cognistream.db`

is created.

### Step 4: Generate Reports

```bash
python src/eda_report.py
```

Check the `reports/` directory for summary CSV files and charts.

### Step 5: Train the Model

```bash
python src/model_training.py
```

Check the `models/` directory for the saved model and evaluation report.

**Note:** These checks apply when the scripts finish successfully. Review terminal errors instead of assuming every output was generated.

## 9. Dashboard Testing

Start the dashboard with:

```bash
python -m streamlit run app.py
```

If necessary, start the visualization page directly:

```bash
python -m streamlit run src/visualize_dashboard.py
```

Manually verify the following:

- The application opens in the browser.
- The dataset preview displays records.
- Developer filters work.
- Date filters work.
- Charts display data.
- Summary tables appear.
- CSV download works.
- No unexpected error messages appear.

## 10. Manual Test Checklist

Use this checklist during project validation.

- [ ] Python runs successfully.
- [ ] Dependencies are installed.
- [ ] The original CSV file is present.
- [ ] Data cleaning completes successfully.
- [ ] Feature engineering completes successfully.
- [ ] SQLite database is created.
- [ ] SQL queries return results.
- [ ] EDA reports and charts are generated.
- [ ] Model training completes.
- [ ] Model evaluation metrics are saved.
- [ ] Dashboard opens successfully.
- [ ] Dashboard filters and download features work.
- [ ] Automated tests have been executed.
- [ ] Errors and limitations are documented.

## 11. Common Testing Problems

### Module Import Error

Confirm that you are running commands from the project root.

If needed, create an empty file:

`src/__init__.py`

For test imports, also confirm that the `tests/` directory contains an empty `__init__.py` if package-style imports are being used.

### Missing Dataset

Verify that this file exists:

`data/developer_activity.csv`

### Missing Processed File

Run the data-cleaning script before running feature engineering or model training.

### Missing Python Package

Install the dependencies again:

```bash
python -m pip install -r requirements.txt
```

### Test Failure

Read the full traceback and identify the failed assertion. Confirm that the test data, expected result, and current implementation agree.

Do not change a test merely to make it pass if the underlying behavior is incorrect.

### Dashboard Error

Check that the required dataset exists, the packages are installed, and the dashboard is launched from the project root.

## 12. Recording Test Results

Record the results of your actual test run.

| Test Area | Status | Notes |
|---|---|---|
| Data cleaning | Pending | Record the actual test result. |
| Feature engineering | Pending | Record the actual test result. |
| SQL operations | Pending | Record the actual test result. |
| Data pipeline | Pending | Record whether each script completed. |
| Machine learning | Pending | Record training and evaluation output. |
| Dashboard | Pending | Record manual verification results. |

Replace `Pending` with `Passed`, `Failed`, or `Not Run` only after checking the relevant result.

## 13. Testing Limitations

- Automated tests cover only the cases explicitly defined in the test files.
- Passing tests do not guarantee that every possible input is handled correctly.
- A working dashboard does not establish that the model is accurate.
- Model results from the small simulated dataset are for demonstration only.
- Focus and cognitive-load indicators are illustrative, not validated psychological measures.

## 14. Conclusion

Testing helps improve the reliability and reproducibility of the CogniStream project.

The combination of automated tests, pipeline checks, SQL validation, and manual dashboard testing provides a structured way to identify errors and prepare the project for review.
