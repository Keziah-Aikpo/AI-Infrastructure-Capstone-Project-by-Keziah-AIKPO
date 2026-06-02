import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Infrastructure Sustainability Dashboard",
    layout="wide"
)

st.title("AI Infrastructure Sustainability Dashboard")

st.write("""
This dashboard presents interactive visualisations for a cross-country panel analysis
of AI-related infrastructure, economic productivity, and environmental sustainability.
""")

from pathlib import Path

df = pd.read_csv(Path(__file__).parent.parent / "data" / "master_panel.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())
