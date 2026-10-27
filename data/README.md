# CogniStream Dataset Documentation

## Overview

This folder contains the datasets used in the CogniStream project to analyze developer activity, focus sessions, interruptions, context switching, and potential cognitive-load indicators.

## Dataset File

`developer_activity.csv`

This dataset will contain simulated developer activity records created for educational and analytical purposes.

## Dataset Columns

| Column | Description |
|---|---|
| timestamp | Date and time of the activity record |
| developer_id | Anonymous identifier for a simulated developer |
| coding_minutes | Minutes spent coding during the interval |
| interruption_count | Number of interruptions recorded |
| context_switches | Number of task or application switches |
| task_complexity | Simulated task complexity score from 1 to 5 |
| break_minutes | Break duration in minutes |
| focus_score | Simulated focus score from 0 to 100 |
| cognitive_load_score | Exploratory workload indicator from 0 to 100 |

## Data Source

The initial dataset will be synthetically generated for this project. It does not represent real employees or actual developer monitoring data.

## Data Preparation

The dataset will be processed using Python and Pandas.

Preparation steps:
1. Check missing values.
2. Remove duplicate records where appropriate.
3. Convert timestamps into datetime format.
4. Validate numerical ranges.
5. Calculate daily and weekly metrics.
6. Prepare features for exploratory analysis and machine learning.

## Usage

The dataset supports:
- Exploratory Data Analysis (EDA)
- Focus-session analysis
- Interruption and context-switching analysis
- Workload indicator visualization
- Experimental machine learning
- Power BI dashboard development

## Privacy and Limitations

Use anonymous or synthetic data. Do not collect personal activity data without informed consent and appropriate authorization.

Focus and cognitive-load scores are illustrative indicators, not clinical measurements or definitive assessments of mental state.

## Project Status

Dataset generation and validation are part of the implementation process.
