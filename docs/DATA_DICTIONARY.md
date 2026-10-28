# CogniStream - Data Dictionary

## 1. Introduction

This document describes the columns used in the CogniStream developer activity dataset.

The dataset contains simulated developer activity records for analyzing coding time, interruptions, context switching, focus scores, and cognitive-load indicators.

**Dataset file:** `data/developer_activity.csv`

**Format:** CSV (Comma-Separated Values)

**Data type:** Simulated sample data for educational and demonstration purposes.

## 2. Dataset Columns

| Column Name | Data Type | Description |
|---|---|---|
| `timestamp` | Datetime | Date and time when the activity record was captured. |
| `developer_id` | String | Anonymous identifier assigned to a simulated developer. |
| `coding_minutes` | Integer | Number of minutes spent coding during the recorded period. |
| `interruption_count` | Integer | Number of interruptions recorded during the period. |
| `context_switches` | Integer | Number of switches between tasks or work contexts. |
| `task_complexity` | Integer | Illustrative task complexity rating on a scale from 1 to 5. |
| `break_minutes` | Integer | Number of minutes spent on breaks during the recorded period. |
| `focus_score` | Numeric | Simulated focus indicator ranging from 0 to 100. |
| `cognitive_load_score` | Numeric | Simulated cognitive-load indicator ranging from 0 to 100. |

## 3. Column Details

### 3.1 timestamp

- **Purpose:** Identifies when the activity record occurred.
- **Example:** `2026-10-20 09:00:00`
- **Usage:** Time-based analysis, daily summaries, and trend charts.

### 3.2 developer_id

- **Purpose:** Separates records belonging to different simulated developers.
- **Example:** `DEV001`
- **Usage:** Comparing activity summaries across developer identifiers.

### 3.3 coding_minutes

- **Purpose:** Records the number of minutes spent coding.
- **Example:** `45`
- **Usage:** Calculating total coding time and comparing activity periods.

### 3.4 interruption_count

- **Purpose:** Records interruptions during a work period.
- **Example:** `2`
- **Usage:** Exploring whether interruptions are associated with changes in focus scores.

### 3.5 context_switches

- **Purpose:** Records how often work shifts between tasks or contexts.
- **Example:** `3`
- **Usage:** Analyzing task-switching patterns and their relationship with other activity indicators.

### 3.6 task_complexity

- **Purpose:** Provides an illustrative rating of task difficulty.
- **Example:** `4`
- **Expected range:** 1 to 5.
- **Usage:** Comparing activity indicators across task-complexity levels.

### 3.7 break_minutes

- **Purpose:** Records time spent on breaks.
- **Example:** `10`
- **Usage:** Exploring activity patterns alongside break duration.

### 3.8 focus_score

- **Purpose:** Represents a simulated focus indicator.
- **Example:** `82`
- **Expected range:** 0 to 100.
- **Usage:** Creating illustrative focus categories and analyzing trends.

### 3.9 cognitive_load_score

- **Purpose:** Represents a simulated cognitive-load indicator.
- **Example:** `65`
- **Expected range:** 0 to 100.
- **Usage:** Exploring workload-related patterns in the sample data.

## 4. Derived Features

The feature-engineering process creates additional columns from the original dataset.

| Derived Feature | Description |
|---|---|
| `hour` | Hour extracted from the timestamp. |
| `day_of_week` | Day of the week associated with the timestamp. |
| `activity_date` | Date extracted from the timestamp. |
| `total_disruptions` | Sum of interruption count and context switches. |
| `focus_category` | Illustrative category based on focus score. |
| `workload_category` | Illustrative category based on cognitive-load score. |

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

These thresholds are project-defined examples, not scientifically validated classifications.

## 5. Data Quality Rules

The data preparation process checks the following conditions:

- Required columns must be present.
- Timestamps must be convertible to datetime values.
- Developer identifiers must not be blank.
- Coding minutes, interruptions, context switches, and break minutes must be non-negative.
- Task complexity must be between 1 and 5.
- Focus and cognitive-load scores must be between 0 and 100.
- Duplicate records should be identified and removed where appropriate.

## 6. Example Use Cases

The dataset can support the following educational analyses:

1. Compare average focus indicators across simulated developers.
2. Explore the relationship between interruptions and focus scores.
3. Examine coding activity by hour or date.
4. Compare activity indicators across task-complexity levels.
5. Build charts for activity and workload-related patterns.
6. Demonstrate a machine-learning classification workflow.

## 7. Privacy and Limitations

- The dataset is simulated and does not represent actual employee monitoring data.
- Developer IDs are sample identifiers, not verified identities.
- Focus and cognitive-load scores are illustrative values.
- Correlation does not establish causation.
- The dataset is too small to support reliable real-world conclusions.
- Results should not be used to evaluate actual employees or make employment decisions.

## 8. Conclusion

This data dictionary defines the meaning, data type, expected range, and intended use of the CogniStream dataset columns. It supports reproducibility, data cleaning, feature engineering, analysis, and project documentation.
