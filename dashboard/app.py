import streamlit as st
import pandas as pd
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

st.subheader("Dataset Preview")
st.dataframe(df.head())
