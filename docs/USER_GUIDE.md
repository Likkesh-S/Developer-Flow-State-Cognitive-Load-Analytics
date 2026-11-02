# CogniStream - User Guide

## 1. Introduction

Welcome to CogniStream!

CogniStream is a developer activity analytics application built using Python, SQL, machine learning, and Streamlit.

It helps users explore simulated developer activity patterns through charts, summary metrics, filters, and analytical reports.

This guide explains how to install, launch, and use the application.

## 2. Application Requirements

Before using CogniStream, make sure you have:

- Windows 10 or Windows 11
- Python 3.10 or newer
- CogniStream project files
- Required Python libraries
- The sample dataset

## 3. Installation

### Step 1: Download the Repository

1. Open the CogniStream GitHub repository.
2. Click the green Code button.
3. Select Download ZIP.
4. Extract the downloaded ZIP file.
5. Open the extracted project folder.

### Step 2: Open Command Prompt

1. Open the project folder.
2. Click the File Explorer address bar.
3. Type `cmd`.
4. Press Enter.

### Step 3: Install Dependencies

Run:

```bash
python -m pip install -r requirements.txt
```

Wait until installation is completed.

For detailed setup instructions, refer to:

`docs/INSTALLATION_GUIDE.md`

## 4. Launching the Application

Open Command Prompt in the project root folder.

Run:

```bash
python -m streamlit run app.py
```

The application should open in your default web browser.

If the home-page navigation does not open the dashboard, launch it directly:

```bash
python -m streamlit run src/visualize_dashboard.py
```

## 5. Understanding the Dashboard

The dashboard provides different ways to explore the simulated activity dataset.

### 5.1 Project Overview

The home page introduces:

- Project name
- Project objectives
- Technologies used
- Dataset overview
- Available analytical features

### 5.2 Summary Metrics

The dashboard displays summary information for the selected records.

Depending on the implementation, this may include:

- Number of activity records
- Average focus score
- Total coding minutes
- Total interruptions

### 5.3 Developer Filter

The developer filter allows users to select one or more developer identifiers.

Use this filter to explore records belonging to a selected simulated developer.

### 5.4 Date Filter

The date filter allows users to select an activity date range.

Use it to explore activity records for a particular period.

### 5.5 Focus Trend Chart

The focus trend chart displays focus scores over time.

It helps users explore how the simulated focus indicator changes across activity records.

### 5.6 Interruptions Versus Focus Chart

This scatter plot compares interruption counts with focus scores.

It helps users investigate possible relationships between the two variables.

A visual relationship does not establish that interruptions cause changes in focus.

### 5.7 Cognitive-Load Indicator Distribution

This chart displays the distribution of simulated cognitive-load scores.

It helps users understand how the sample values are spread across the dataset.

### 5.8 Developer Summary

The summary table provides aggregated activity information for the selected records.

It can help compare coding activity and other indicators across developer identifiers.

### 5.9 Filtered Dataset Preview

Users can inspect the records that match the selected filters.

### 5.10 CSV Download

If the download option is available, users can export the filtered dataset as a CSV file for additional analysis.

## 6. Running the Data Pipeline

For the latest generated outputs, run the processing scripts from the project root in this order:

### Step 1: Data Cleaning

```bash
python src/data_cleaning.py
```

### Step 2: Feature Engineering

```bash
python src/feature_engineering.py
```

### Step 3: SQLite Data Loading

```bash
python src/load_data_to_sqlite.py
```

### Step 4: EDA Reports

```bash
python src/eda_report.py
```

### Step 5: Machine Learning

```bash
python src/model_training.py
```

### Step 6: Launch Dashboard

```bash
python -m streamlit run app.py
```

## 7. Understanding the Activity Indicators

| Indicator | Meaning |
|---|---|
| Coding Minutes | Time spent coding in the sample activity period |
| Interruptions | Number of recorded interruptions |
| Context Switches | Number of switches between tasks or work contexts |
| Task Complexity | Illustrative task rating from 1 to 5 |
| Break Minutes | Time spent on breaks |
| Focus Score | Simulated focus indicator from 0 to 100 |
| Cognitive Load Score | Simulated workload-related indicator from 0 to 100 |

These values are illustrative and should not be treated as validated measurements of an individual's psychological state or productivity.

## 8. Troubleshooting

### Problem 1: Python Command Not Found

Try:

```bash
py --version
```

If Python is not installed, install it and reopen Command Prompt.

### Problem 2: Missing Dataset

Check whether this file exists:

`data/developer_activity.csv`

### Problem 3: Missing Libraries

Run:

```bash
python -m pip install -r requirements.txt
```

### Problem 4: Dashboard Does Not Start

Try:

```bash
python -m streamlit run src/visualize_dashboard.py
```

### Problem 5: Processed Files Are Missing

Run the data-cleaning and feature-engineering scripts before launching components that depend on their outputs.

## 9. Stopping the Application

To stop Streamlit:

1. Return to the Command Prompt window.
2. Press `Ctrl + C`.
3. Wait for the application process to stop.

## 10. Responsible Use

CogniStream uses simulated data for educational purposes.

The application should not be used to:

- Diagnose a person's mental condition.
- Rank real employees.
- Make employment decisions.
- Claim that a focus score proves productivity.
- Draw conclusions about individuals without appropriate evidence.

## 11. Conclusion

This user guide provides the basic steps for installing and operating CogniStream.

Users can explore sample activity records, apply filters, view analytical charts, and download data for further analysis.

The application demonstrates how data analytics and visualization technologies can be combined in a practical project.
