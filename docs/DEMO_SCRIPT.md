# CogniStream – Project Demonstration Script

## 1. Introduction

Good morning everyone.

Today, I am going to demonstrate my project titled **CogniStream: Developer Flow-State & Cognitive Load Analytics**.

This project uses data analytics and machine learning techniques to analyze simulated developer activity patterns, including coding duration, interruptions, context switching, focus indicators, and workload indicators.

The main objective is to transform activity data into meaningful visual insights using Python, SQL, machine learning, and Streamlit.

## 2. Project Overview

First, I will explain the project structure.

The project contains the following folders:

- data
- notebooks
- src
- sql
- tests
- models
- reports
- docs

Each folder has a specific purpose in the project workflow.

## 3. Dataset Demonstration

Next, I will demonstrate the dataset.

Dataset name: `developer_activity.csv`

The dataset contains:

- Developer ID
- Timestamp
- Coding minutes
- Interruption count
- Context switches
- Task complexity
- Break minutes
- Focus score
- Cognitive load score

This is simulated data prepared for educational and analytical purposes.

## 4. Data Cleaning Demonstration

Now I will demonstrate the data cleaning process.

Python and Pandas are used to:

- Check missing values.
- Remove duplicate records.
- Validate numerical values.
- Convert timestamps.
- Check the valid ranges of scores.

**Command:**

```bash
python src/data_cleaning.py
```

**Expected output:**

A cleaned dataset is generated inside:

`data/processed/developer_activity_cleaned.csv`

Show the actual terminal output during the demonstration.

## 5. Feature Engineering Demonstration

Next, I will demonstrate feature engineering.

The program creates additional columns such as:

- Hour
- Day of the week
- Activity date
- Total disruptions
- Focus category
- Workload indicator category

**Command:**

```bash
python src/feature_engineering.py
```

**Expected output:**

- `developer_activity_features.csv`
- `daily_developer_summary.csv`

These files are stored in `data/processed/`.

## 6. SQL Database Demonstration

Now I will demonstrate the SQL database.

The project uses SQLite to store and analyze developer activity records.

**Command:**

```bash
python src/load_data_to_sqlite.py
```

Database file:

`data/cognistream.db`

The SQL queries demonstrate:

- Retrieving developer records.
- Total coding minutes.
- Average focus scores.
- Interruption summaries.
- Daily developer activity.

Open `sql/analysis_queries.sql` to show the queries.

## 7. Exploratory Data Analysis Demonstration

Next, I will demonstrate exploratory data analysis.

**Command:**

```bash
python src/eda_report.py
```

The program generates charts and reports to explore:

- Focus scores by developer.
- Interruptions versus focus.
- Cognitive load indicator distribution.
- Developer activity summaries.

Show the actual charts generated in the `reports/` folder.

## 8. Machine Learning Demonstration

Now I will explain the machine learning component.

The project uses the Random Forest Classifier to demonstrate focus category classification.

The categories are:

- Low
- Moderate
- High

**Command:**

```bash
python src/model_training.py
```

The model produces evaluation information such as:

- Accuracy.
- Classification report.
- Confusion matrix.

The trained model is saved in:

`models/focus_classifier.joblib`

The evaluation results are saved in:

`models/model_metrics.txt`

These results are demonstrations using a small simulated dataset and should not be interpreted as validated real-world performance.

## 9. Streamlit Dashboard Demonstration

This is the main interactive part of my project.

**Command:**

```bash
python -m streamlit run app.py
```

If the home page navigation does not work, I can launch the dashboard directly:

```bash
python -m streamlit run src/visualize_dashboard.py
```

The dashboard displays:

- Total activity records.
- Average focus indicator.
- Average workload indicator.
- Focus trends.
- Interruptions versus focus.
- Cognitive load indicator distribution.
- Developer activity summaries.

I can also demonstrate the developer and date filters.

## 10. Testing Demonstration

The project includes automated tests for:

- Data cleaning.
- Feature engineering.
- SQL queries.

**Command:**

```bash
python -m unittest discover -s tests -v
```

Show the actual test results in the terminal.

## 11. Conclusion

Through this demonstration, I have shown how developer activity data can be cleaned, processed, stored, analyzed, and visualized.

The project combines Python, SQL, machine learning, and Streamlit to demonstrate a complete data analytics workflow.

Thank you.

## 12. Questions and Answers

### Q1. What is CogniStream?

CogniStream is a data analytics project that explores simulated developer activity patterns using Python, SQL, machine learning, and visualization.

### Q2. Why did you choose Python?

Python provides useful libraries such as Pandas, NumPy, Matplotlib, and Scikit-learn for data analysis and machine learning.

### Q3. What is the purpose of SQL?

SQL is used to store, retrieve, filter, and summarize structured developer activity data.

### Q4. Which machine learning algorithm is used?

The project uses the Random Forest Classifier to demonstrate focus category classification.

### Q5. What is the purpose of Streamlit?

Streamlit is used to develop an interactive dashboard for displaying analytical results.

### Q6. Is the dataset real?

No. The current project uses simulated data for educational and demonstration purposes.

### Q7. What are the future improvements?

Future improvements include larger representative datasets, improved model validation, additional dashboard features, and privacy-conscious real-time analytics.

---

## Important Presentation Notes

- Run the project before the review.
- Keep the dataset ready.
- Open the GitHub repository.
- Keep the dashboard ready in your browser.
- Show actual output screenshots.
- Do not present expected outputs as completed results.
- Explain that focus and workload scores are illustrative indicators, not clinical measurements.
