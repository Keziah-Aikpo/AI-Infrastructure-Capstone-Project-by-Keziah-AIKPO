import streamlit as st
import pandas as pd
from pathlib import Path

# Page settings
st.set_page_config(
    page_title="AI Infrastructure Sustainability Dashboard",
    layout="wide"
)

# Title
st.title("AI Infrastructure Sustainability Dashboard")

st.write("""
This dashboard presents interactive visualisations for a cross-country panel analysis
of AI-related infrastructure, economic productivity, and environmental sustainability.
""")

# Load data
csv_path = Path(__file__).parent.parent / "data" / "data" / "master_panel.csv"

df = pd.read_csv(csv_path)

# Clean column names for display
df.columns = df.columns.str.replace("_", " ")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())
