# AI-Infrastructure-Capstone-Project-by-Keziah-AIKPO
AI Infrastructure Sustainability and Economic Capstone Project
Developed a cross-country panel data analysis of 32 countries (2010–2021) examining the relationship between AI-related infrastructure, economic productivity, and environmental sustainability. Applied econometric techniques and fixed-effects regression models to analyze productivity, carbon intensity, renewable energy adoption, electricity consumption, and carbon taxation

## Repository Structure

### dashboard/

Contains the interactive Streamlit dashboard developed as a companion portfolio artefact.

Key features include: Country-level exploration, Productivity trends, Carbon intensity trends, Renewable energy trends, Electricity consumption trends, Country rankings and Interactive sustainability visualisations

### data/

Contains both the individual datasets used in the study and the final merged panel dataset.

Files include:

* labour_productivity.csv
* carbon_intensity.csv
* electricity_consumption.csv
* renewable_energy_share.csv
* carbon_tax.csv
* master_panel.csv

The master_panel.csv dataset is the final dataset used for descriptive analysis, correlation analysis, and fixed-effects regression modelling.

### figures/

Stores figures, diagrams, visualisations, and conceptual frameworks used throughout the project and dissertation.

Examples include: Correlation heatmaps, Conceptual frameworks, Sustainability visualisations and AI infrastructure diagrams

### notebooks/

Contains the complete analytical workflow used throughout the project.

* 01_data_cleaning.ipynb - Data cleaning and preprocessing of individual datasets.
* 02_merge_datasets.ipynb – Construction of the final cross-country panel dataset.
* 03_analysis_and_regressions.ipynb – Descriptive statistics, correlation analysis, and regression modelling.
* 99_final_submission.ipynb – Final consolidated notebook containing the complete workflow, results, visualisations, and interpretations.

### results/

Stores analytical outputs generated during the study.

Examples include: Descriptive statistics, Correlation matrices, Regression outputs and Model summaries

## Methodology

The study employs a cross-country panel dataset covering 32 countries between 2010 and 2021.

Two-Way Fixed Effects models are used to examine the relationships between: Labour Productivity, Carbon Intensity, Renewable Energy Share, Electricity Consumption and Carbon Taxation

## Interactive Dashboard

The Streamlit dashboard provides an interactive environment for exploring the study's findings and visualising the relationships between productivity, sustainability, energy systems, and AI-related infrastructure development.
