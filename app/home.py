import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.metrics import get_summary_stats
from utils.visuals import plot_score_trend

st.set_page_config(page_title="Golf Tracker", layout="wide")

st.title("⛳ Golf Performance Dashboard")

# Load data
summary_df, rounds_df, course_df = load_data()

# Summary cards
stats = get_summary_stats(summary_df)
col1, col2, col3 = st.columns(3)
col1.metric("Best Score", stats["best_score"], stats["best_course"])
col2.metric("Average Score", stats["avg_score"])
col3.metric("Avg vs Par", f"{stats['avg_diff']:+}")

st.divider()

st.subheader("📈 Score Trend Over Time")
fig = plot_score_trend(summary_df)
st.pyplot(fig)

st.subheader("🏌️ Recent Rounds")
st.dataframe(summary_df.sort_values("Date", ascending=False).head(5))
