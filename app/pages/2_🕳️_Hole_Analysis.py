import streamlit as st
from utils.data_loader import load_user_data
import pandas as pd
import matplotlib.pyplot as plt

st.title("🕳️ Hole Analysis")

summary_df, rounds_df, course_df = load_user_data()
course_list = rounds_df["Course"].unique()
selected_course = st.selectbox("Select Course", course_list)

merged = rounds_df.merge(course_df, on=["Course", "Hole"], how="left")
merged["Diff"] = merged["Score"] - merged["Par"]

course_summary = merged[merged["Course"] == selected_course].groupby("Hole").agg(
    Avg_Score=("Score", "mean"),
    Par=("Par", "first"),
    Avg_Diff=("Diff", "mean")
).reset_index()

st.dataframe(course_summary)

fig, ax = plt.subplots()
ax.bar(course_summary["Hole"], course_summary["Avg_Diff"])
ax.axhline(0, color="gray", linestyle="--")
ax.set_title(f"Average Score Difference per Hole — {selected_course}")
ax.set_xlabel("Hole")
ax.set_ylabel("Average vs Par")
st.pyplot(fig)
