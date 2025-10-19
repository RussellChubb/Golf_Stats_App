import streamlit as st
from utils.data_loader import load_user_data
from utils.visuals import plot_score_trend

st.title("📈 Performance Trends")

summary_df, _, _ = load_user_data()
fig = plot_score_trend(summary_df)
st.pyplot(fig)

st.write("Coming soon: rolling averages, per-course trends, and improvement stats.")
