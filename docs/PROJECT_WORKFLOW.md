# CogniStream Project Workflow

## 1. Project Overview

CogniStream is a developer activity analytics project that uses
Python, SQL, machine learning, and interactive visualization to
explore coding activity, interruptions, context switching, and
simulated focus and cognitive-load indicators.

The project uses a simulated dataset for educational and analytical
purposes.

## 2. Problem Statement

Developer work involves multiple activities, including coding,
handling interruptions, switching between tasks, and taking breaks.
Understanding these activity patterns can help explore how work
habits relate to recorded focus indicators.

CogniStream organizes this information into an analytical workflow
that produces summaries, charts, and a demonstration machine
learning model.

## 3. Project Objectives

- Organize developer activity data.
- Clean and validate the dataset.
- Create useful analytical features.
- Analyze focus and interruption patterns.
- Store activity records in an SQL database.
- Train a demonstration focus-category classifier.
- Create an interactive analytics dashboard.
- Test important components of the pipeline.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and application logic |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Static visualizations |
| Plotly | Interactive charts |
| Streamlit | Dashboard application |
| SQLite | Relational data storage |
| SQL | Data retrieval and analysis |
| Scikit-learn | Demonstration machine learning model |
| GitHub | Source control and documentation |
| unittest | Automated testing |

## 5. Workflow Architecture

```text
Simulated Activity Dataset
          |
          v
Data Validation and Cleaning
          |
          v
Feature Engineering
          |
          +----------------------+
          |                      |
          v                      v
     SQLite Database       Analytical Dataset
          |                      |
          v                      v
      SQL Analysis        Exploratory Analysis
                                 |
                                 v
                        Machine Learning Demo
                                 |
                                 v
                       Streamlit Visualization
                                 |
                                 v
                         Results and Reports
```

## 6. Step 1: Data Preparation

The input dataset is stored at:

`data/developer_activity.csv`

It includes fields such as:

- Timestamp
- Developer ID
- Coding minutes
- Interruption count
- Context switches
- Task complexity
- Break minutes
- Focus score
- Cognitive-load score

The records are simulated rather than collected from actual
developers.

## 7. Step 2: Data Cleaning

The script `src/data_cleaning.py` checks required columns, converts
data types, removes duplicate records, and filters invalid values.

Expected output:

`data/processed/developer_activity_cleaned.csv`

## 8. Step 3: Feature Engineering

The script `src/feature_engineering.py` derives:

- Hour of activity
- Day of the week
- Activity date
- Total disruptions
- Focus categories
- Illustrative workload categories
- Daily developer summaries

Expected outputs:

- `data/processed/developer_activity_features.csv`
- `data/processed/daily_developer_summary.csv`

## 9. Step 4: SQL Database

The SQL schema is defined in:

`sql/create_tables.sql`

Analysis queries are stored in:

`sql/analysis_queries.sql`

The script `src/load_data_to_sqlite.py` loads the source CSV into
the SQLite database:

`data/cognistream.db`

Queries summarize coding time, focus scores, interruptions,
context switching, and daily activity.

## 10. Step 5: Exploratory Data Analysis

The script `src/eda_report.py` generates summary statistics,
developer-level summaries, charts, and a correlation matrix.

Reports are written to the `reports/` directory.

## 11. Step 6: Machine Learning

The script `src/model_training.py` trains a Random Forest classifier
to predict categories derived from the simulated focus score.

The model and evaluation output are saved under `models/`.

Because the dataset is small and synthetic, the model is a
demonstration of the machine learning workflow, not a validated
real-world prediction system.

## 12. Step 7: Dashboard

The application entry point is `app.py`.

The dashboard implementation is `src/visualize_dashboard.py`.

It displays summary metrics, focus trends, interruptions,
cognitive-load indicator distributions, and developer comparisons.

Run the application from the repository root:

`python -m streamlit run app.py`

## 13. Step 8: Testing

The `tests/` directory contains unit tests for:

- Data cleaning
- Feature engineering
- SQL database operations

Run the tests with:

`python -m unittest discover -s tests -v`

## 14. Expected Project Deliverables

- Documented source code
- Simulated activity dataset
- Cleaned and transformed datasets
- SQLite database
- SQL analysis queries
- Exploratory data analysis reports
- Demonstration machine learning model
- Interactive Streamlit dashboard
- Automated tests
- GitHub project documentation

## 15. Limitations

- The current dataset is simulated.
- Focus and cognitive-load scores are illustrative metrics.
- Correlation does not establish causation.
- The machine learning model requires larger, representative,
  independently validated data before any real-world use.
- Results should not be interpreted as clinical or psychological
  assessments.

## 16. Conclusion

CogniStream demonstrates an end-to-end analytics workflow using
Python, SQL, machine learning, testing, and visualization.

The project provides a foundation for learning how data can be
prepared, analyzed, stored, modeled, and presented through an
interactive dashboard.
