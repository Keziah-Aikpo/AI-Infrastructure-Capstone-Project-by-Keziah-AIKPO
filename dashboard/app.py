import streamlit as st
from pathlib import Path

st.write("Current file:")
st.write(__file__)

st.write("Dashboard folder contents:")
st.write(list(Path(__file__).parent.iterdir()))

st.write("Repository root contents:")
st.write(list(Path(__file__).parent.parent.iterdir()))
