
# CogniStream – Project Presentation

## Slide 1: Title

**Project Title:** CogniStream: Developer Flow-State & Cognitive Load Analytics

**Project Domain:** Data Analytics and Machine Learning

**Technologies:** Python, SQL, Machine Learning, Streamlit, SQLite

**Presentation:** Academic Project Review

---

## Slide 2: Introduction

- Developers work on multiple software development tasks.
- Interruptions and context switching are common during development.
- Understanding developer activity patterns can help improve work planning.
- CogniStream analyzes simulated developer activity data using analytics techniques.

**Main Idea:** Transform developer activity data into meaningful analytical insights.

---

## Slide 3: Problem Statement

- Developer activity information can be difficult to analyze manually.
- Frequent interruptions and task switching may affect work patterns.
- Data needs to be organized before meaningful analysis.
- A structured analytics solution is required to visualize activity trends.

**Proposed Solution:** Develop an analytics pipeline with data processing, SQL, machine learning, and an interactive dashboard.

---

## Slide 4: Project Objectives

1. Analyze developer activity data.
2. Identify interruption and context-switching patterns.
3. Calculate focus and workload indicators.
4. Perform data cleaning and feature engineering.
5. Store and retrieve data using SQL.
6. Apply machine learning classification.
7. Build an interactive dashboard.

---

## Slide 5: Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Matplotlib | Visualization |
| Seaborn | Statistical charts |
| Scikit-learn | Machine learning |
| SQLite | Database |
| SQL | Data analysis |
| Streamlit | Dashboard |
| Plotly | Interactive charts |
| GitHub | Version control |

---

## Slide 6: Dataset Description

**Dataset Name:** developer_activity.csv

Dataset columns:

- timestamp
- developer_id
- coding_minutes
- interruption_count
- context_switches
- task_complexity
- break_minutes
- focus_score
- cognitive_load_score

**Dataset Type:** Simulated data for educational and analytical purposes.

---

## Slide 7: System Architecture

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

---

## Slide 8: Data Cleaning

Data cleaning is performed using Python and Pandas.

Activities:

- Identify missing values.
- Remove duplicate records.
- Validate numerical values.
- Convert timestamps.
- Check score ranges.
- Generate a cleaned dataset.

**Output:** developer_activity_cleaned.csv

---

## Slide 9: Feature Engineering

New features are created from existing columns.

Examples:

- Hour of activity.
- Day of the week.
- Activity date.
- Total disruptions.
- Focus category.
- Workload indicator category.

**Purpose:** Prepare useful variables for analysis and visualization.

---

## Slide 10: Exploratory Data Analysis

The project explores:

- Average focus score.
- Coding duration.
- Interruption patterns.
- Context switching.
- Cognitive load indicator distribution.
- Developer activity summaries.

**Output:** Charts, summary tables, and analytical reports.

---

## Slide 11: SQL Database Analysis

SQLite is used for structured data storage.

SQL operations include:

- Creating database tables.
- Loading developer activity records.
- Retrieving records.
- Calculating total coding minutes.
- Finding average focus scores.
- Summarizing interruptions.
- Generating daily summaries.

**Output:** cognistream.db

---

## Slide 12: Machine Learning

**Algorithm:** Random Forest Classifier

**Target:** Focus category

Categories:

- Low
- Moderate
- High

Evaluation methods:

- Accuracy score.
- Classification report.
- Confusion matrix.

**Purpose:** Demonstrate a machine learning classification workflow using simulated data.

---

## Slide 13: Interactive Dashboard

The Streamlit dashboard displays:

- Total activity records.
- Average focus indicator.
- Average workload indicator.
- Focus trends.
- Interruptions versus focus.
- Cognitive load indicator distribution.
- Developer summaries.

**Purpose:** Make analytical information easier to understand.

---

## Slide 14: Project Outputs

Expected project deliverables:

1. Cleaned dataset.
2. Feature-engineered dataset.
3. SQL database.
4. Exploratory analysis reports.
5. Data visualization charts.
6. Machine learning model.
7. Model evaluation metrics.
8. Interactive dashboard.
9. Automated test results.

Include screenshots of the outputs that you have actually generated.

---

## Slide 15: Results and Findings

Add actual results after running the project.

| Metric | Actual Result |
|---|---|
| Total records | [Enter value] |
| Cleaned records | [Enter value] |
| Number of developers | [Enter value] |
| Average focus score | [Enter value] |
| Total interruptions | [Enter value] |
| Model accuracy | [Enter value] |
| Tests passed | [Enter value] |

**Important:** Do not invent results. Use values from your actual program output.

---

## Slide 16: Limitations

- Dataset is simulated.
- Dataset size is limited.
- Focus and workload scores are illustrative indicators.
- Machine learning results require further validation.
- Correlation does not prove causation.
- The project is not a clinical assessment or employee monitoring system.

---

## Slide 17: Future Enhancements

- Larger representative datasets.
- Real-time analytics with suitable consent.
- Improved machine learning models.
- Additional dashboard features.
- Automated report generation.
- Enhanced privacy and security.
- Automated testing and deployment.

---

## Slide 18: Conclusion

CogniStream demonstrates how data analytics, SQL, machine learning, and visualization can be combined to analyze developer activity patterns.

The project provides a complete learning workflow covering data cleaning, feature engineering, exploratory analysis, database operations, model training, and dashboard development.

Further research and validation using suitable real-world data would be needed before drawing conclusions about actual developer experiences.

---

## Slide 19: Thank You

**Thank You!**

Project: CogniStream – Developer Flow-State & Cognitive Load Analytics

**Questions and Discussion**
