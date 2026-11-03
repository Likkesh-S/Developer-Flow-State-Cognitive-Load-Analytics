# CogniStream: Developer Flow-State & Cognitive Load Analytics

## 1. Abstract

CogniStream is a data analytics project designed to study developer activity patterns, focus indicators, interruptions, context switching, and workload indicators using data analytics and machine learning techniques.

The project uses a simulated developer activity dataset containing information such as coding duration, interruption count, context switches, task complexity, break duration, focus score, and cognitive load score.

Python is used for data cleaning, feature engineering, exploratory data analysis, and machine learning. SQL is used for structured data storage and analysis. Streamlit provides an interactive dashboard for visualizing developer activity patterns.

The project demonstrates how data analytics techniques can organize activity data and identify patterns that may help teams understand work processes.

**Note:** The dataset is simulated. Focus and cognitive load scores are illustrative indicators, not clinical measurements or definitive assessments of a person's mental state.

## 2. Introduction

Software developers frequently work on tasks that require concentration, problem-solving, and continuous interaction with development tools.

Interruptions, frequent task switching, and complex assignments can affect work patterns. Understanding these factors through data analysis can help organizations explore productivity trends and improve work planning.

CogniStream applies Python, SQL, machine learning, and dashboard visualization to analyze simulated developer activity data.

## 3. Problem Statement

Understanding developer activity patterns can be challenging when information about coding time, interruptions, task complexity, and context switching is stored in separate records.

Without structured analysis, it can be difficult to identify trends and compare activity patterns.

CogniStream addresses this problem by developing a data analytics workflow that cleans, processes, analyzes, and visualizes developer activity information.

## 4. Objectives

- Analyze developer activity records.
- Measure coding duration and interruption patterns.
- Examine context switching and task complexity.
- Explore focus and workload indicators.
- Perform data cleaning and feature engineering.
- Apply machine learning for demonstration purposes.
- Store and analyze records using SQL.
- Develop an interactive Streamlit dashboard.
- Present analytical findings through reports and charts.

## 5. Scope of the Project

The project focuses on analyzing simulated developer activity data.

The scope includes:

- Dataset preparation and validation.
- Data preprocessing using Python.
- Exploratory data analysis.
- Feature engineering.
- SQL-based data storage and querying.
- Machine learning classification.
- Interactive dashboard development.
- Testing and documentation.

The project does not monitor real employees or make clinical or employment decisions.

## 6. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning |
| SQLite | Database storage |
| SQL | Data retrieval and analysis |
| Streamlit | Interactive dashboard |
| Plotly | Interactive charts |
| Jupyter Notebook | Data exploration |
| GitHub | Project version control |

## 7. Dataset Description

The project uses a simulated dataset named `developer_activity.csv`.

The dataset contains the following columns:

| Column | Description |
|---|---|
| timestamp | Date and time of activity |
| developer_id | Developer reference identifier |
| coding_minutes | Time spent coding |
| interruption_count | Number of interruptions |
| context_switches | Number of task switches |
| task_complexity | Task complexity indicator |
| break_minutes | Break duration |
| focus_score | Illustrative focus indicator |
| cognitive_load_score | Illustrative workload indicator |

The dataset is intended for learning, testing, and demonstrating analytics techniques.

## 8. System Architecture

The project follows this workflow:

1. Dataset collection or preparation.
2. Data cleaning and validation.
3. Feature engineering.
4. Database loading.
5. Exploratory data analysis.
6. Machine learning model training.
7. Dashboard development.
8. Testing and reporting.

### Architecture Flow

CSV Dataset
    |
    v
Data Cleaning
    |
    v
Feature Engineering
    |
    +------> SQLite Database
    |
    v
Exploratory Data Analysis
    |
    v
Machine Learning
    |
    v
Streamlit Dashboard
    |
    v
Reports and Insights

## 9. Methodology

### 9.1 Data Preparation

A simulated dataset is prepared with developer activity records. The dataset contains numerical indicators and timestamps.

### 9.2 Data Cleaning

Python and Pandas are used to:

- Check missing values.
- Remove duplicate records.
- Validate numerical values.
- Convert timestamps into date-time format.
- Check valid score ranges.
- Prepare cleaned data for further analysis.

### 9.3 Feature Engineering

Additional features are created to support analysis.

Examples include:

- Hour of activity.
- Day of the week.
- Activity date.
- Total disruptions.
- Focus category.
- Workload indicator category.

### 9.4 Exploratory Data Analysis

Exploratory analysis is performed to understand:

- Average focus scores.
- Developer coding duration.
- Interruption patterns.
- Context switching.
- Cognitive load indicator distribution.
- Relationships between activity variables.

### 9.5 SQL Analysis

SQLite is used to store developer activity records.

SQL queries are used to calculate totals, averages, daily summaries, and developer-level metrics.

### 9.6 Machine Learning

A Random Forest classification model is used to demonstrate the classification of focus categories.

The model uses activity-related variables to predict categories derived from the simulated focus score.

Model evaluation includes accuracy, classification reports, and a confusion matrix.

Because the dataset is small and simulated, model performance should not be treated as evidence of real-world predictive accuracy.

### 9.7 Dashboard Development

Streamlit is used to create an interactive dashboard.

The dashboard presents:

- Key activity metrics.
- Focus trends.
- Interruptions versus focus.
- Cognitive load indicator distribution.
- Developer summaries.
- Filtered activity records.

## 10. Project Implementation

The project is organized into the following folders:

- `data/` – Dataset and processed data.
- `notebooks/` – Data exploration and focus analysis.
- `src/` – Python implementation files.
- `sql/` – Database schema and analysis queries.
- `tests/` – Automated test files.
- `models/` – Saved machine learning model and metrics.
- `reports/` – Generated analysis reports and charts.
- `docs/` – Project documentation.

The main application is launched through `app.py`.

## 11. Expected Outputs

The project is designed to generate:

1. Cleaned developer activity dataset.
2. Feature-engineered dataset.
3. Daily developer summary.
4. Exploratory data analysis reports.
5. Data visualization charts.
6. SQLite database.
7. Trained Random Forest model.
8. Model evaluation report.
9. Interactive Streamlit dashboard.
10. Automated test results.

These are expected deliverables. Include only outputs that have actually been generated when preparing the final submission.

## 12. Results and Findings

Record the actual results after executing the complete project.

### Results Table

| Analysis | Actual Result |
|---|---|
| Total dataset records | [Enter result] |
| Records after cleaning | [Enter result] |
| Number of developers | [Enter result] |
| Average focus score | [Enter result] |
| Total interruptions | [Enter result] |
| Average cognitive load score | [Enter result] |
| Model accuracy | [Enter result] |
| Automated tests passed | [Enter result] |

### Observations

Add observations based on the actual charts and generated reports.

Do not assume that interruptions cause lower focus or that a higher workload indicator represents a clinical condition. Describe only patterns observed in the dataset.

## 13. Testing

Testing is performed using Python's unittest framework.

The project includes tests for:

- Data cleaning.
- Feature engineering.
- SQL queries.

The application can also be checked manually by opening the Streamlit dashboard and testing its filters, charts, and data display.

Record the actual test results in the final submission.

## 14. Limitations

- The current dataset is simulated.
- The number of records is limited.
- Focus and workload indicators are illustrative.
- Machine learning results may not generalize to real developers.
- Correlation does not establish causation.
- The dashboard depends on the availability of the project dataset and generated files.
- The system is not intended for employee surveillance or individual performance scoring.

## 15. Future Enhancements

Possible future improvements include:

- Use of larger and representative datasets.
- Integration with real-time activity data where appropriate consent and privacy protections exist.
- Improved machine learning evaluation.
- More interactive dashboard features.
- Additional SQL reports.
- Automated testing through GitHub Actions.
- Improved data security and access controls.
- More detailed trend analysis.

## 16. Conclusion

CogniStream demonstrates the use of Python, SQL, machine learning, and data visualization to analyze developer activity patterns.

The project provides a structured workflow for data preparation, cleaning, feature engineering, exploratory analysis, database operations, model training, and dashboard development.

It also demonstrates how analytics tools can be combined in a practical project. Further validation using suitable, consent-based real-world data would be required before drawing conclusions about actual developer experiences.

## 17. References

- Python Documentation: https://docs.python.org/3/
- Pandas Documentation: https://pandas.pydata.org/docs/
- NumPy Documentation: https://numpy.org/doc/
- Scikit-learn Documentation: https://scikit-learn.org/stable/
- SQLite Documentation: https://www.sqlite.org/docs.html
- Streamlit Documentation: https://docs.streamlit.io/
- Plotly Documentation: https://plotly.com/python/

---

**Project Name:** CogniStream: Developer Flow-State & Cognitive Load Analytics

**Project Type:** Data Analytics and Machine Learning

**Report Version:** 1.0

**Status:** Academic Project Documentation
