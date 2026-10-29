# CogniStream - Project Methodology

## 1. Introduction

CogniStream is a data analytics project designed to explore simulated developer activity, focus indicators, interruptions, context switching, and cognitive-load indicators.

The project follows a structured data analytics methodology using Python, SQL, machine learning, and dashboard visualization.

## 2. Project Objectives

The main objectives are:

- Analyze simulated developer activity records.
- Identify patterns in coding time and interruptions.
- Explore relationships between focus scores and activity indicators.
- Transform raw data into useful analytical features.
- Demonstrate a basic machine-learning classification workflow.
- Present findings through visualizations and an interactive dashboard.

## 3. Research Approach

The project uses a quantitative, exploratory data analytics approach.

Numerical activity records are processed and summarized to identify patterns and relationships. The analysis is intended for educational demonstration rather than scientific or clinical conclusions.

## 4. Data Collection

### Dataset Source

The project uses a simulated CSV dataset:

`data/developer_activity.csv`

The dataset contains sample records with the following information:

- Timestamp
- Developer identifier
- Coding minutes
- Interruption count
- Context switches
- Task complexity
- Break minutes
- Focus score
- Cognitive-load score

### Data Collection Method

The dataset is prepared for demonstration and does not represent actual developer monitoring data. The focus and cognitive-load scores are illustrative values.

## 5. Data Preprocessing

The raw dataset is checked and prepared before analysis.

### Steps

1. Load the CSV file using Pandas.
2. Verify that the required columns exist.
3. Convert timestamps into datetime values.
4. Convert numerical columns into suitable numeric types.
5. Handle invalid or missing records.
6. Remove duplicate records where appropriate.
7. Check numerical ranges and data consistency.
8. Save the cleaned dataset for later stages.

### Output

`data/processed/developer_activity_cleaned.csv`

## 6. Exploratory Data Analysis

Exploratory Data Analysis (EDA) is used to understand the dataset before building the model.

### Analysis Activities

- Calculate descriptive statistics.
- Summarize coding time by developer.
- Calculate average focus scores.
- Examine interruption and context-switching patterns.
- Explore relationships between numerical variables.
- Identify possible data-quality issues.

### Visualizations

The project generates charts such as:

- Focus indicators by developer
- Interruptions versus focus scores
- Cognitive-load indicator distribution

### Output

Summary tables and charts are stored in the `reports/` directory.

## 7. Feature Engineering

Feature engineering creates additional variables that help organize the activity data.

### Features Created

- `hour`: hour extracted from the timestamp.
- `day_of_week`: day associated with the activity timestamp.
- `activity_date`: date extracted from the timestamp.
- `total_disruptions`: interruption count plus context switches.
- `focus_category`: Low, Moderate, or High.
- `workload_category`: Lower Indicator, Moderate Indicator, or Higher Indicator.

### Focus Category Rules

| Focus Score | Category |
|---|---|
| 0–59 | Low |
| 60–79 | Moderate |
| 80–100 | High |

### Workload Category Rules

| Cognitive-Load Score | Category |
|---|---|
| 0–39 | Lower Indicator |
| 40–69 | Moderate Indicator |
| 70–100 | Higher Indicator |

These categories are illustrative and are not validated psychological classifications.

### Output

- `data/processed/developer_activity_features.csv`
- `data/processed/daily_developer_summary.csv`

## 8. SQL Database Management

SQLite is used to demonstrate relational data storage and SQL-based analysis.

### Activities

1. Create the developer activity table.
2. Define data types and basic validation constraints.
3. Load cleaned records into the database.
4. Execute SQL queries to summarize activity.
5. Retrieve results for reporting and analysis.

### Database

`data/cognistream.db`

### Example SQL Analysis

- Total coding minutes by developer
- Average focus score by developer
- Total interruptions and context switches
- Average indicators by task complexity
- Daily activity summaries

## 9. Machine Learning Methodology

A Random Forest classifier is used to demonstrate how activity indicators can be used to predict an illustrative focus category.

### Model Development Steps

1. Load the engineered dataset.
2. Define the input features.
3. Define the target category from the simulated focus score.
4. Split the dataset into training and testing subsets.
5. Handle missing feature values using median imputation.
6. Train the Random Forest classifier.
7. Generate predictions on the test subset.
8. Evaluate predictions using accuracy, precision, recall, F1-score, and a confusion matrix.
9. Save the trained model and evaluation results.

### Input Features

- Coding minutes
- Interruption count
- Context switches
- Task complexity
- Break minutes
- Cognitive-load score

### Target Variable

`focus_category`

### Model Output

- `models/focus_classifier.joblib`
- `models/model_metrics.txt`

### Important Limitation

The target categories are derived from the simulated focus score. The dataset is small, so model metrics are only a demonstration of the machine-learning workflow. They do not establish real-world predictive performance.

## 10. Dashboard Development

Streamlit is used to build an interactive dashboard for exploring the dataset.

### Dashboard Features

- Dataset overview
- Summary metrics
- Developer filtering
- Date filtering
- Focus trends over time
- Interruptions versus focus scatter plot
- Cognitive-load indicator distribution
- Developer summary table
- Filtered data preview
- CSV download

### Application Files

- `app.py`
- `src/visualize_dashboard.py`

### Run the Dashboard

```bash
python -m streamlit run app.py
```

If needed, launch the visualization page directly:

```bash
python -m streamlit run src/visualize_dashboard.py
```

## 11. Testing and Validation

Testing helps verify that important parts of the project behave as expected.

The project includes tests for:

- Data cleaning rules
- Duplicate handling
- Feature engineering
- SQL queries
- Basic database validation

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

Test results should be reviewed before presenting the project as complete.

## 12. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and model development |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Charts and visualizations |
| Scikit-learn | Machine learning |
| SQLite | Database storage and querying |
| SQL | Data retrieval and aggregation |
| Streamlit | Interactive dashboard |
| GitHub | Version control and project documentation |

## 13. Project Workflow

The project follows this sequence:

1. Prepare the simulated dataset.
2. Clean and validate the data.
3. Perform exploratory data analysis.
4. Engineer additional features.
5. Load records into SQLite.
6. Execute SQL analysis queries.
7. Train and evaluate the demonstration classifier.
8. Generate reports and visualizations.
9. Launch the Streamlit dashboard.
10. Run tests and document limitations.

## 14. Ethical Considerations

Developer activity indicators can be misleading when interpreted without context.

This project uses simulated data and should not be used to monitor, rank, diagnose, or make employment decisions about real people. Focus and cognitive-load scores are not clinical measures, and observed correlations do not prove causation.

## 15. Conclusion

The methodology demonstrates an end-to-end analytics workflow, from dataset preparation through data processing, SQL analysis, machine learning, visualization, and testing.
