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

csv_path = Path(__file__).parent.parent / "data" / "data" / "master_panel.csv"

df = pd.read_csv(csv_path)

df.columns = df.columns.str.replace("_", " ")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Country Selector")

countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "Select a country",
    countries
)

country_data = df[df["Country"] == selected_country]

st.write(f"Showing data for **{selected_country}**")

st.dataframe(country_data)

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
