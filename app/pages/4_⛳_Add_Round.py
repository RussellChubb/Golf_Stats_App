import streamlit as st
import pandas as pd
from datetime import date
from utils.data_loader import load_user_data, save_data
from streamlit_option_menu import option_menu

# --Navbar--
page = option_menu(
    menu_title=None,  # Hide the title
    options=[
        "Home",
        "Hole Analysis",
        "Add Round",
        "Round Summary",
        "GitHub",
    ],
    icons=[
        "house-fill",
        "flag-fill",
        "plus-circle-fill",
        "bar-chart-fill",
        "github",
    ],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": "transparent",
            "max-width": "100%",  # Make it full width
        },
        "icon": {"color": "rgba(46,204,113,0.9)", "font-size": "18px"},
        "nav-link": {
            "font-family": "'Space Grotesk', sans-serif",
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "padding": "12px 30px",  # Increased padding for wider buttons
            "background-color": "transparent",
            "border-bottom": "2px solid transparent",
            "color": "#ffffff",
            "flex": "1",  # Makes each button take equal width
        },
        "nav-link-selected": {
            "background-color": "rgba(46,204,113,0.2)",
            "border-bottom": "2px solid rgba(46,204,113,0.9)",
            "color": "#ffffff",
            "font-weight": "600",
        },
        "nav-link:hover": {
            "background-color": "rgba(46,204,113,0.1)",
            "border-bottom": "2px solid rgba(46,204,113,0.5)",
        },
    },
)

summary_df, rounds_df, course_df = load_user_data()

st.title("⛳ Add New Round")

with st.form("new_round_form"):
    st.subheader("Round Summary Info")
    col1, col2, col3 = st.columns(3)
    course = col1.selectbox("Course", course_df["Course"].unique())
    player = col2.text_input("Player Name", "Russell")
    round_date = col3.date_input("Date", date.today())
    round_type = col1.selectbox("Round Type", ["Front-9", "Back-9", "Full", "Practice"])
    comment = st.text_input("Comment", "")

    st.subheader("Enter Scores")
    holes = course_df[course_df["Course"] == course][["Hole", "Par", "Distance"]].copy()
    holes["Score"] = holes["Hole"].apply(
        lambda h: st.number_input(
            f"Hole {h} Score", min_value=1, max_value=15, value=4, step=1
        )
    )

    submitted = st.form_submit_button("Add Round")

if submitted:
    total_score = holes["Score"].sum()
    total_par = holes["Par"].sum()
    diff = total_score - total_par

    # Append to summary table
    new_summary = pd.DataFrame(
        [
            {
                "Date": round_date,
                "Course": course,
                "Player": player,
                "RoundType": round_type,
                "Score": total_score,
                "ParTotal": total_par,
                "ScoreDiff": diff,
                "Comment": comment,
            }
        ]
    )
    summary_df = pd.concat([summary_df, new_summary], ignore_index=True)

    # Append to rounds data
    new_rounds = holes.assign(
        Course=course,
        Player=player,
        Date=round_date,
    )[["Course", "Hole", "Player", "Score", "Date"]]
    rounds_df = pd.concat([rounds_df, new_rounds], ignore_index=True)

    save_data(summary_df, rounds_df, course_df)

    st.success(f"New round added for {player} at {course} ({round_type})!")
