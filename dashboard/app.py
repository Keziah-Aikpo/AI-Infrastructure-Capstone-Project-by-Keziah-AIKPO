import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="AI Infrastructure Sustainability Dashboard",
    layout="wide"
)

st.title("Sustainable and Economic AI Infrastructure Dashboard")

st.write("""
This dashboard presents interactive visualisations for a cross-country panel analysis
of AI-related infrastructure, economic productivity, and environmental sustainability.
""")

st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Countries", 32)
col2.metric("Years", "2010-2021")
col3.metric("Observations", 369)

# Load data
csv_path = Path(__file__).parent.parent / "data" / "data" / "master_panel.csv"
df = pd.read_csv(csv_path)

# Clean column names
df.columns = df.columns.str.replace("_", " ")

st.subheader("Country Rankings")

ranking_metric = st.selectbox(
    "Select a ranking metric",
  [
    "Labour Productivity",
    "Carbon Intensity",
    "Renewable Share",
    "Electricity Consumption",
    "Carbon Tax"
]
)

country_rankings = (
    df.groupby("Country")[ranking_metric]
      .mean()
      .reset_index()
      .sort_values(by=ranking_metric, ascending=False)
)

country_rankings.index = range(1, len(country_rankings) + 1)

st.dataframe(
    country_rankings,
    use_container_width=True
)


# Dataset preview
st.subheader("Dataset Preview")

preview_country = st.selectbox(
    "Select a country to preview",
    sorted(df["Country"].unique()),
    key="preview_country"
)

preview_data = df[df["Country"] == preview_country]

st.dataframe(preview_data)

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

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Productivity (Output Per Worker)",
    round(country_data["Labour Productivity"].mean(), 2)
)

col2.metric(
    "Carbon Intensity (gCO₂/kWh)",
    round(country_data["Carbon Intensity"].mean(), 2)
)

col3.metric(
    "Renewable Share (%)",
    round(country_data["Renewable Share"].mean(), 2)
)

col4.metric(
    "Electricity Consumption (TWh)",
    round(country_data["Electricity Consumption"].mean(), 2)
)

col5.metric(
    "Carbon Tax (€/tCO₂)",
    round(country_data["Carbon Tax"].mean(), 2)
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

fig_electricity = px.line(
    country_data,
    x="Year",
    y="Electricity Consumption",
    markers=True,
    title=f"Electricity Consumption in {selected_country} (TWh)"
)

st.plotly_chart(fig_electricity, use_container_width=True)

# Renewable Share VS Carbon Intensity

# Create continent groups

continent_map = {
    # Europe
    "Austria": "Europe",
    "Belgium": "Europe",
    "Denmark": "Europe",
    "Estonia": "Europe",
    "Finland": "Europe",
    "France": "Europe",
    "Germany": "Europe",
    "Greece": "Europe",
    "Hungary": "Europe",
    "Iceland": "Europe",
    "Italy": "Europe",
    "Latvia": "Europe",
    "Lithuania": "Europe",
    "Luxembourg": "Europe",
    "Netherlands": "Europe",
    "Norway": "Europe",
    "Poland": "Europe",
    "Portugal": "Europe",
    "Slovenia": "Europe",
    "Spain": "Europe",
    "Sweden": "Europe",
    "Switzerland": "Europe",
    "United Kingdom": "Europe",

    # North America
    "Canada": "North America",
    "Costa Rica": "North America",
    "Mexico": "North America",
    "United States": "North America",

    # South America
    "Chile": "South America",
    "Colombia": "South America",

    # Asia
    "Japan": "Asia",

    # Oceania
    "Australia": "Oceania",
    "New Zealand": "Oceania"
}

df["Continent"] = df["Country"].map(continent_map)

st.subheader("Renewable Share vs Carbon Intensity")

st.write("""
This scatter plot illustrates the relationship between Renewable Energy Share and Carbon Intensity across the countries included in the study. Each point represents a country-year observation between 2010 and 2021. The downward pattern of the data indicates a strong negative relationship, meaning that countries with higher shares of renewable energy generally tend to exhibit lower carbon intensity. This finding supports the dissertation's conclusion that cleaner energy systems are associated with improved environmental sustainability outcomes. """)

fig_scatter_carbon = px.scatter(
    df,
    x="Renewable Share",
    y="Carbon Intensity",
    color="Continent",
    hover_data=["Country", "Year"],
    title="Renewable Share and Carbon Intensity"
)

fig_scatter_carbon.update_layout(
    height=700
)

st.plotly_chart(fig_scatter_carbon, use_container_width=True)

# Renewable Share VS Labour Productivity

st.subheader("Renewable Share vs Labour Productivity")

st.write("""
This scatter plot examines whether countries with higher renewable energy adoption
also tend to exhibit stronger labour productivity outcomes.
""")

fig_productivity_scatter = px.scatter(
    df,
    x="Renewable Share",
    y="Labour Productivity",
    color="Country",
    hover_data=["Country", "Year"],
    title="Renewable Share and Labour Productivity"
)

fig_productivity_scatter.update_layout(
    height=700
)

st.plotly_chart(fig_productivity_scatter, use_container_width=True)


st.header("Key Findings")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    📉 Environmental Finding

    Renewable Energy Share was the strongest determinant of Carbon Intensity.
    Countries with higher renewable energy adoption tended to exhibit significantly
    lower Carbon Intensity, highlighting the importance of cleaner energy systems.
    """)

with col2:
    st.success("""
    📈 Economic Finding

    Renewable Energy Share was also the only variable significantly associated
    with Labour Productivity. Countries with higher renewable energy adoption
    tended to exhibit stronger productivity performance.
    """)

col3, col4 = st.columns(2)

with col3:
    st.info("""
    ⚡ Energy-System Finding

    Electricity Consumption and Carbon Taxation were not statistically significant
    predictors of Carbon Intensity. Environmental outcomes appear to depend more
    on how electricity is generated than on how much electricity is consumed.
    """)

with col4:
    st.info("""
    🤖 AI Infrastructure Implication

    The findings suggest that AI infrastructure can support both economic
    productivity and environmental sustainability when powered by cleaner
    and more sustainable energy systems.
    """)
