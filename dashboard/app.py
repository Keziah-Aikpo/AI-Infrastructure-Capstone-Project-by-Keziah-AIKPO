import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="AI Infrastructure Sustainability Dashboard",
    layout="wide"
)

st.title("AI Infrastructure Sustainability Dashboard")

st.write("""
This dashboard presents interactive visualisations for a cross-country panel analysis
of AI-related infrastructure, economic productivity, and environmental sustainability.
""")

# Load data
csv_path = Path(__file__).parent.parent / "data" / "data" / "master_panel.csv"
df = pd.read_csv(csv_path)

# Clean column names
df.columns = df.columns.str.replace("_", " ")

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Country selector
st.subheader("Country Selector")

countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "Select a country",
    countries
)

country_data = df[df["Country"] == selected_country]

# Key statistics
st.subheader(f"Key Statistics: {selected_country}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Productivity",
    round(country_data["Labour Productivity"].mean(), 2)
)

col2.metric(
    "Average Carbon Intensity",
    round(country_data["Carbon Intensity"].mean(), 2)
)

col3.metric(
    "Average Renewable Share (%)",
    round(country_data["Renewable Share"].mean(), 2)
)

# Country trends
st.subheader(f"Country Trends: {selected_country}")

fig_productivity = px.line(
    country_data,
    x="Year",
    y="Labour Productivity",
    markers=True,
    title=f"Labour Productivity in {selected_country}"
)

st.plotly_chart(fig_productivity, use_container_width=True)

fig_carbon = px.line(
    country_data,
    x="Year",
    y="Carbon Intensity",
    markers=True,
    title=f"Carbon Intensity in {selected_country}"
)

st.plotly_chart(fig_carbon, use_container_width=True)

fig_renewable = px.line(
    country_data,
    x="Year",
    y="Renewable Share",
    markers=True,
    title=f"Renewable Energy Share in {selected_country}"
)

st.plotly_chart(fig_renewable, use_container_width=True)

st.subheader("Renewable Share vs Carbon Intensity")

st.write("""
This scatter plot visualises the relationship between renewable energy adoption and carbon intensity.
The study found a strong negative correlation of approximately -0.596, suggesting that countries
with higher renewable energy shares generally tend to have lower carbon intensity.
""")

fig_scatter_carbon = px.scatter(
    df,
    x="Renewable Share",
    y="Carbon Intensity",
    color="Country",
    hover_data=["Country", "Year"],
    trendline="ols",
    title="Renewable Share and Carbon Intensity"
)

st.plotly_chart(fig_scatter_carbon, use_container_width=True)
