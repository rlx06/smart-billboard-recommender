import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# ---------- Page Config ----------
st.set_page_config(
    page_title="Smart Billboard Recommender",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS for dark mode and styling ----------
st.markdown("""
<style>
body {
    background-color: #1e1e1e;
    color: #fafafa;
}
.big-font {
    font-size: 26px !important;
    font-weight: bold;
}
.header-font {
    font-size: 20px !important;
    font-weight: 500;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title and Introduction ----------
st.title("🎯 Smart Billboard Recommender System")
st.markdown('<p class="big-font">Find the best billboards for your next ad campaign</p>', unsafe_allow_html=True)

st.image("https://source.unsplash.com/1600x400/?billboard,advertising", use_column_width=True)

st.markdown("""
This app helps advertisers select **optimal billboard placements** by analyzing:
- 👥 Target Audience
- 👣 Foot Traffic
- 📍 Location
- 💰 Budget
""")

# ---------- Load Data ----------
billboards_df = pd.read_csv("data/billboards_dataset.csv")
advertisers_df = pd.read_csv("data/advertisers_dataset.csv")
recommendations = pd.read_csv("data/top_recommendations_ADV001.csv")  # example

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📈 Recommendations", "📊 Analytics Dashboard", "📄 About Project"])

# ---------- Tab 1: Recommendations ----------
with tab1:
    st.header("📈 Top Billboard Recommendations")
    st.dataframe(recommendations.style.highlight_max(axis=0))

    st.download_button("⬇️ Download Recommendations", data=recommendations.to_csv(index=False), file_name="recommendations.csv")

# ---------- Tab 2: Analytics ----------
with tab2:
    st.header("📊 Billboard Data Insights")
    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        top_cities = billboards_df['city'].value_counts().head(10)
        sns.barplot(x=top_cities.values, y=top_cities.index, ax=ax1, palette="cool")
        ax1.set_title("Top Cities by Billboard Count")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        sns.histplot(billboards_df['estimated_footfall'], bins=20, kde=True, color="orange", ax=ax2)
        ax2.set_title("Distribution of Foot Traffic")
        st.pyplot(fig2)

    st.markdown('<p class="header-font">📍 Billboard Types by Environment</p>', unsafe_allow_html=True)
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    type_env = billboards_df.groupby(['type', 'environment']).size().unstack().fillna(0)
    type_env.plot(kind='bar', stacked=True, ax=ax3, colormap='magma')
    st.pyplot(fig3)

# ---------- Tab 3: About ----------
with tab3:
    st.header("📄 About the Project")
    st.write("""
This project recommends billboards for advertisers using criteria like budget, foot traffic, and location.

Built with:
- 🐍 Python
- 📊 Pandas & Matplotlib
- 🌐 Streamlit for UI
- 🤖 Simple scoring algorithm

Team: Your Name / University / Course (edit this section!)
    """)
