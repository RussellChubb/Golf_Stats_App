import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    summary = pd.read_excel("data/Summary_Data.xlsx", sheet_name="Summary", parse_dates=["Date"])
    rounds = pd.read_excel("data/Rounds_Data.xlsx", sheet_name="Rounds", parse_dates=["Date"])
    course = pd.read_excel("data/Course_Data.xlsx", sheet_name="Course")

    # Clean basic formatting
    for df in [summary, rounds, course]:
        df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Add derived column for score diff (if missing)
    if "Plus_/_Minus" in summary.columns:
        summary["ScoreDiff"] = summary["Plus_/_Minus"]
    elif "ScoreDiff" not in summary.columns:
        summary["ScoreDiff"] = summary["Score"] - summary["Par_for_Course"]

    return summary, rounds, course

import os

def save_data(summary_df, rounds_df, course_df, path="data"):
    """Save updated dataframes to CSV."""
    os.makedirs(path, exist_ok=True)
    summary_df.to_csv(f"{path}/course_summary.csv", index=False)
    rounds_df.to_csv(f"{path}/rounds_data.csv", index=False)
    course_df.to_csv(f"{path}/course_data.csv", index=False)

from utils.session_manager import get_current_user

def load_user_data():
    summary_df, rounds_df, course_df = load_data()
    user = get_current_user()
    if user:
        summary_df = summary_df[summary_df["Player"] == user]
        rounds_df = rounds_df[rounds_df["Player"] == user]
    return summary_df, rounds_df, course_df
