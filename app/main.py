import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_country_data, get_summary_stats

# --------------------------
# Page configuration
# --------------------------
st.set_page_config(
    page_title="Solar Energy Dashboard",
)

# --------------------------
# Sidebar controls
# --------------------------
st.sidebar.header("Controls")
countries = ["benin", "sierraleone", "togo"]
selected_countries = st.sidebar.multiselect(
    "Select countries:",
    countries,
    default=countries
)

metric = st.sidebar.selectbox(
    "Select metric:",
    ["GHI", "DNI", "DHI", "Tamb"]
)

show_summary = st.sidebar.checkbox("Show Summary Statistics", value=True)

# --------------------------
# Load Data
# --------------------------
if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()

dfs = [load_country_data(c) for c in selected_countries]
df_all = pd.concat(dfs, ignore_index=True)

# --------------------------
# Header
# --------------------------
st.title("Solar Energy Dashboard")
st.write("Compare solar metrics across countries.")

# --------------------------
# Summary Statistics
# --------------------------
if show_summary:
    st.subheader("Summary Statistics by Country")
    summary_table = (
        df_all.groupby("Country")[["GHI", "DNI", "DHI", "Tamb"]]
        .agg(["mean", "median", "std"])
        .round(2)
    )
    st.dataframe(summary_table)

# --------------------------
# Boxplot
# --------------------------
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df_all, x="Country", y=metric, palette="Set2", ax=ax)
ax.set_xlabel("Country")
ax.set_ylabel(metric)
ax.set_title(f"{metric} Distribution")
st.pyplot(fig)

# --------------------------
# Correlation Heatmap
# --------------------------
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(6, 4))
corr_cols = ["GHI", "DNI", "DHI", "Tamb"]
sns.heatmap(df_all[corr_cols].corr(), annot=True, cmap="Blues", fmt=".2f", ax=ax)
st.pyplot(fig)

# --------------------------
# Bubble chart: GHI vs Tamb (Bubble = RH)
# --------------------------
st.subheader("Temperature vs GHI (Bubble = RH)")
fig, ax = plt.subplots(figsize=(8, 4))
for country in selected_countries:
    df_c = df_all[df_all["Country"] == country.replace("_", " ").title()]
    ax.scatter(df_c["Tamb"], df_c["GHI"], s=df_c["RH"], alpha=0.5, label=country.title())
ax.set_xlabel("Ambient Temperature (°C)")
ax.set_ylabel("GHI (W/m²)")
ax.set_title("GHI vs Temperature")
ax.legend()
st.pyplot(fig)

# --------------------------
# Footer
# --------------------------
st.markdown("---")
st.caption("10 Academy Solar Challenge Week 1 Dashboard prepared by Tsegaye Shewamare")
