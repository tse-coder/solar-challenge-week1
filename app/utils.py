import pandas as pd
import streamlit as st

@st.cache_data
def load_country_data(country: str) -> pd.DataFrame:
    """Load cleaned solar dataset for a given country."""
    path = f"data/{country}_clean.csv"
    df = pd.read_csv(path)
    df["Country"] = country.replace("_", " ").title()
    return df

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return summary statistics for solar metrics."""
    return df[["GHI", "DNI", "DHI", "Tamb"]].describe().T
