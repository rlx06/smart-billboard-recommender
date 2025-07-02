import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Billboard Recommender", layout="wide")

st.title("🎯 Smart Billboard Recommender System")
st.markdown("""
Welcome to the Smart Billboard Recommender!  
This tool suggests the **best billboards** for your ad campaign based on **target audience**, **estimated footfall**, **location**, and **budget**.
""")
# Load data
billboards = pd.read_csv("data/billboards_dataset.csv")
advertisers = pd.read_csv("data/advertisers_dataset.csv")

st.title("📍 Smart Billboard Recommender")

# Sidebar: Select advertiser
advertiser_name = st.sidebar.selectbox("Select Advertiser", advertisers["advertiser_id"])

# Get advertiser info
selected_adv = advertisers[advertisers["advertiser_id"] == advertiser_name].iloc[0]

# Calculate scores
def score(billboard):
    audience_score = 1 if billboard["preferred_audience"] == selected_adv["target_audience"] else 0.5
    budget_score = 1 if billboard["monthly_cost"] <= selected_adv["budget"] else 0
    footfall_score = billboard["estimated_footfall"] / 20000
    return round((audience_score * 0.4 + budget_score * 0.3 + footfall_score * 0.3), 3)

billboards["score"] = billboards.apply(score, axis=1)

# Show results
st.subheader(f"Top Billboard Matches for {advertiser_name}")
st.dataframe(billboards.sort_values(by="score", ascending=False).head(10))