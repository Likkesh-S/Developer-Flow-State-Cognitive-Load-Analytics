
# CogniStream - API and Module Reference

## 1. Introduction

This document describes the main Python modules, SQL files, notebooks, and application entry points used in the CogniStream project.

The project is organized into separate modules to make the code easier to understand, maintain, test, and extend.

## 2. Project Structure

```text
cognistream-developer-analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── developer_activity.csv
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_focus_analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── load_data_to_sqlite.py
│   ├── eda_report.py
│   └── visualize_dashboard.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── tests/
│   ├── test_data_cleaning.py
│   ├── test_feature_engineering.py
│   └── test_sql_queries.py
│
├── docs/
│
├── models/
└── reports/
```

This is a logical overview. Some folders and generated files appear only after the corresponding scripts have been run.

## 3. Main Application Module

### 3.1 app.py

**Purpose:** Provides the main Streamlit application page.

Responsibilities:

- Display project information.
- Present an overview of the dataset.
- Show project summary information.
- Provide navigation to the visualization dashboard.
- Display available report files.

Run command:

```bash
python -m streamlit run app.py
```

## 4. Data Processing Modules

### 4.1 data_cleaning.py

**Location:** `src/data_cleaning.py`

**Purpose:** Cleans and validates the original dataset.

Main responsibilities:

- Read the original CSV file.
- Check required columns.
- Convert data types.
- Handle invalid records.
- Remove duplicates.
- Save cleaned data.

Output:

`data/processed/developer_activity_cleaned.csv`

Run:

```bash
python src/data_cleaning.py
```

### 4.2 feature_engineering.py

**Location:** `src/feature_engineering.py`

**Purpose:** Creates additional analytical features.

Main responsibilities:

- Extract hour and date information.
- Generate day-of-week values.
- Calculate total disruptions.
- Assign illustrative focus categories.
- Assign illustrative workload categories.
- Create daily developer summaries.

Outputs:

- `data/processed/developer_activity_features.csv`
- `data/processed/daily_developer_summary.csv`

Run:

```bash
python src/feature_engineering.py
```

## 5. Database Module

### 5.1 load_data_to_sqlite.py

**Location:** `src/load_data_to_sqlite.py`

**Purpose:** Loads validated activity records into an SQLite database.

Main responsibilities:

- Read the original CSV dataset.
- Validate records.
- Connect to SQLite.
- Create the database table using the SQL schema.
- Insert activity records.

Output:

`data/cognistream.db`

Run:

```bash
python src/load_data_to_sqlite.py
```

**Important:** Running this loader again replaces the existing records in the target table.

## 6. Exploratory Data Analysis Module

### 6.1 eda_report.py

**Location:** `src/eda_report.py`

**Purpose:** Generates statistical summaries and visual reports.

Main responsibilities:

- Calculate descriptive statistics.
- Summarize developer activity.
- Generate a correlation matrix.
- Create focus-related charts.
- Visualize interruption patterns.
- Display the distribution of cognitive-load indicators.

Outputs are saved in:

`reports/`

Run:

```bash
python src/eda_report.py
```

## 7. Machine Learning Module

### 7.1 model_training.py

**Location:** `src/model_training.py`

**Purpose:** Trains a Random Forest classifier for an illustrative focus category.

Main responsibilities:

- Load engineered data.
- Select input features.
- Prepare the target category.
- Split data into training and testing subsets.
- Handle missing feature values.
- Train the classifier.
- Evaluate model predictions.
- Save the trained model and metrics.

Outputs:

- `models/focus_classifier.joblib`
- `models/model_metrics.txt`

Run:

```bash
python src/model_training.py
```

The classifier is a demonstration using simulated data. Its predictions should not be treated as validated measurements of real developer focus.

## 8. Dashboard Module

### 8.1 visualize_dashboard.py

**Location:** `src/visualize_dashboard.py`

**Purpose:** Displays interactive analytics using Streamlit.

Main responsibilities:

- Load the activity dataset.
- Filter records by developer.
- Filter records by date.
- Display summary metrics.
- Generate focus trend charts.
- Display interruption comparisons.
- Show cognitive-load indicator distributions.
- Provide CSV downloads.

Run:

```bash
python -m streamlit run src/visualize_dashboard.py
```

## 9. SQL Files

### 9.1 create_tables.sql

**Location:** `sql/create_tables.sql`

Purpose:

- Create the developer activity table.
- Define database columns.
- Apply basic validation constraints.
- Create indexes for common queries.

The schema is designed for SQLite.

### 9.2 analysis_queries.sql

**Location:** `sql/analysis_queries.sql`

Purpose:

Contains SQL queries for:

- Viewing activity records.
- Calculating coding-time totals.
- Calculating average focus scores.
- Summarizing interruptions.
- Analyzing task complexity.
- Creating daily summaries.

## 10. Testing Modules

### 10.1 test_data_cleaning.py

Tests data cleaning behavior, including duplicate removal and invalid values.

### 10.2 test_feature_engineering.py

Tests the creation of derived features and illustrative categories.

### 10.3 test_sql_queries.py

Tests database insertion, aggregation, and validation behavior using a temporary SQLite database.

Run all tests:

```bash
python -m unittest discover -s tests -v
```

## 11. Notebook Modules

### 11.1 01_data_exploration.ipynb

Purpose:

- Load the dataset.
- Inspect rows and columns.
- Check missing values.
- Calculate descriptive statistics.
- Generate basic charts.

### 11.2 02_focus_analysis.ipynb

Purpose:

- Create focus categories.
- Summarize activity by developer.
- Explore focus patterns by hour.
- Compare interruptions with focus scores.
- Export analysis results.

These notebooks provide an interactive environment for exploratory analysis.

## 12. Dependencies

The main libraries used by the project include:

| Library | Purpose |
|---|---|
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning |
| Streamlit | Dashboard development |
| Plotly | Interactive charts |
| SQLAlchemy | SQL toolkit |
| Jupyter | Interactive notebooks |

Install the dependencies using:

```bash
python -m pip install -r requirements.txt
```

## 13. Module Execution Order

For the main processing workflow, execute:

1. `src/data_cleaning.py`
2. `src/feature_engineering.py`
3. `src/load_data_to_sqlite.py`
4. `src/eda_report.py`
5. `src/model_training.py`
6. `app.py` to launch the dashboard

Run automated tests separately when needed.

## 14. Limitations

- The project uses simulated sample data.
- Module descriptions reflect the current project implementation.
- The project does not provide a public REST API.
- The machine-learning model is for educational demonstration.
- Focus and cognitive-load scores are illustrative indicators, not clinical measurements.
- Actual results depend on the data and successful execution of each module.

## 15. Conclusion

This module reference provides an overview of the CogniStream codebase.

It explains how the Python scripts, notebooks, SQL files, testing modules, and dashboard work together to demonstrate a complete data analytics workflow.
