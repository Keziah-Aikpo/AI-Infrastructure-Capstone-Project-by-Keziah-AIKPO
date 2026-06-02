import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="AI Infrastructure Sustainability Dashboard",
    layout="wide"
)

st.title("AI Infrastructure Sustainable and Economic Challenges Dashboard")

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
