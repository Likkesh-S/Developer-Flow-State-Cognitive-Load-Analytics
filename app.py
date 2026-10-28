"""CogniStream main application entry point."""

from pathlib import Path
import subprocess
import sys

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent
DASHBOARD_FILE = PROJECT_ROOT / "src" / "visualize_dashboard.py"
REPORT_DIR = PROJECT_ROOT / "reports"
DATA_FILE = PROJECT_ROOT / "data" / "developer_activity.csv"

st.set_page_config(
    page_title="CogniStream | Home",
    page_icon="📊",
    layout="wide",
)

st.title("CogniStream")
st.subheader("Developer Flow-State & Cognitive Load Analytics")

st.markdown(
    """
    Welcome to **CogniStream**, a data analytics project that explores
    developer activity patterns using Python, SQL, machine learning,
    and interactive visualizations.

    The project uses simulated data to study coding activity,
    interruptions, context switching, focus scores, and illustrative
    cognitive-load indicators.
    """
)

st.divider()

# Project overview
st.header("Project Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Core Tools", "Python + SQL")
col2.metric("Analytics", "EDA + ML")
col3.metric("Visualization", "Streamlit")

st.divider()

# Navigation
st.header("Explore the Project")

st.markdown(
    """
    - **Analytics Dashboard:** Explore developer activity and charts.
    - **Dataset:** Check whether the source CSV is available.
    - **Reports:** Open generated analysis files.
    - **Project Documentation:** Read the repository README.
    """
)

if st.button("Open Analytics Dashboard", type="primary"):
    if DASHBOARD_FILE.exists():
        st.switch_page("src/visualize_dashboard.py")
    else:
        st.error(
            "Dashboard file not found. Check "
            "src/visualize_dashboard.py."
        )

st.divider()

# Dataset status
st.header("Dataset Status")

if DATA_FILE.exists():
    st.success("Source dataset found: data/developer_activity.csv")

    if st.button("Preview Dataset"):
        import pandas as pd

        data = pd.read_csv(DATA_FILE)
        st.write(f"Records: {len(data)}")
        st.dataframe(data.head(10), use_container_width=True)
else:
    st.warning(
        "Source dataset not found. Add "
        "data/developer_activity.csv to the project."
    )

st.divider()

# Generated reports
st.header("Generated Reports")

if REPORT_DIR.exists():
    report_files = sorted(
        file for file in REPORT_DIR.iterdir()
        if file.is_file()
    )

    if report_files:
        for report in report_files:
            st.write(f"📄 {report.name}")
    else:
        st.info(
            "No reports generated yet. Run "
            "python src/eda_report.py."
        )
else:
    st.info(
        "The reports folder will be populated when you "
        "run the exploratory data analysis script."
    )

st.divider()

st.caption(
    "Academic project demonstration. The dataset is simulated, "
    "and focus and cognitive-load scores are illustrative indicators, "
    "not validated psychological measurements."
)
