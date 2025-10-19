import streamlit as st
from utils.data_loader import load_user_data

summary_df, rounds_df, course_df = load_user_data()

st.title("📊 Round Summary")

selected_round_date = st.selectbox("Select Round Date", summary_df["Date"].dt.strftime("%Y-%m-%d").unique())
selected_course = summary_df.loc[summary_df["Date"].dt.strftime("%Y-%m-%d") == selected_round_date, "Course"].values[0]

st.subheader(f"Round Details — {selected_course} ({selected_round_date})")

round_data = rounds_df[(rounds_df["Course"] == selected_course) & (rounds_df["Date"].dt.strftime("%Y-%m-%d") == selected_round_date)]
st.dataframe(round_data[["Hole", "Score"]])
