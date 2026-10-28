import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

ROOT = Path(_file_).resolve().parent.parent
st.title("📊 Data Analytics Dashboard")
st.write("Explore your dataset, analyze data quality, and visualize trends.")

# Find CSV files in the repository
csv_files = list(ROOT.glob(".csv")) + list(ROOT.glob("data//.csv"))

# Sidebar
st.sidebar.header("Dashboard Settings")

if not csv_files:
    st.warning(
        "No CSV dataset found. Add your CSV file to the repository root "
        "or inside a data folder."
    )
    st.info(
        "Your dashboard code is ready. Upload a CSV dataset to start "
        "exploring your data."
    )
    st.stop()

selected_file = st.sidebar.selectbox(
    "Select dataset",
    csv_files,
    format_func=lambda p: str(p.relative_to(ROOT))
)

try:
    df = pd.read_csv(selected_file)
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()

# Data overview
st.subheader("📌 Dataset Overview")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Rows", f"{df.shape[0]:,}")
c2.metric("Total Columns", f"{df.shape[1]:,}")
c3.metric("Missing Values", f"{df.isna().sum().sum():,}")
c4.metric("Duplicate Rows", f"{df.duplicated().sum():,}")

# Dataset preview
st.subheader("📋 Dataset Preview")

search = st.text_input("Search all columns")
filtered_df = df.copy()

if search:
    mask = filtered_df.astype(str).apply(
        lambda col: col.str.contains(search, case=False, na=False)
    ).any(axis=1)
    filtered_df = filtered_df[mask]

st.dataframe(filtered_df, use_container_width=True)

st.download_button(
    "⬇️ Download displayed data as CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="dashboard_data.csv",
    mime="text/csv"
)

# Column analysis
st.subheader("🔍 Column Analysis")

numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

tab1, tab2, tab3, tab4 = st.tabs([
    "Charts", "Missing Values", "Statistics", "Correlations"
])

with tab1:
    chart_type = st.selectbox(
        "Chart type",
        ["Histogram", "Bar Chart", "Scatter Plot", "Box Plot"]
    )

    if chart_type == "Histogram":
        if numeric_cols:
            col = st.selectbox("Numeric column", numeric_cols)
            fig = px.histogram(df, x=col, title=f"Distribution of {col}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns available.")

    elif chart_type == "Bar Chart":
        available = categorical_cols or df.columns.tolist()
        col = st.selectbox("Category column", available)
        counts = df[col].astype(str).value_counts().head(20)
        fig = px.bar(
            x=counts.index,
            y=counts.values,
            labels={"x": col, "y": "Count"},
            title=f"Top values in {col}"
        )
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Scatter Plot":
        if len(numeric_cols) >= 2:
            x = st.selectbox("X-axis", numeric_cols)
            y = st.selectbox(
                "Y-axis",
                [c for c in numeric_cols if c != x]
            )
            fig = px.scatter(df, x=x, y=y, title=f"{y} vs {x}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("At least two numeric columns are required.")

    elif chart_type == "Box Plot":
        if numeric_cols:
            col = st.selectbox("Column to inspect", numeric_cols)
            fig = px.box(df, y=col, title=f"Box Plot: {col}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns available.")

with tab2:
    st.write("Missing values in each column")
    missing = df.isna().sum().sort_values(ascending=False)
    missing = missing[missing > 0]

    if missing.empty:
        st.success("No missing values found.")
    else:
        missing_df = missing.rename("Missing Count").reset_index()
        missing_df.columns = ["Column", "Missing Count"]
        missing_df["Missing %"] = (
            missing_df["Missing Count"] / len(df) * 100
        ).round(2)

        st.dataframe(missing_df, use_container_width=True)
        fig = px.bar(
            missing_df,
            x="Column",
            y="Missing Count",
            title="Missing Values by Column"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.write("Descriptive statistics")
    st.dataframe(
        df.describe(include="all").transpose(),
        use_container_width=True
    )

with tab4:
    if len(numeric_cols) >= 2:
        corr = df[numeric_cols].corr()
        fig = px.imshow(
            corr,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title="Numeric Feature Correlations"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("At least two numeric columns are required.")

st.caption("Data Analytics Dashboard | Built with Streamlit and Plotly")
