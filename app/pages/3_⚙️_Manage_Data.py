import streamlit as st
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

st.title("⚙️ Manage Data")

summary_df, rounds_df, course_df = load_user_data()

tab1, tab2, tab3 = st.tabs(["Course Summary", "Rounds Data", "Course Data"])

with tab1:
    edited_summary = st.data_editor(summary_df, num_rows="dynamic", key="summary_edit")

with tab2:
    edited_rounds = st.data_editor(rounds_df, num_rows="dynamic", key="rounds_edit")

with tab3:
    edited_course = st.data_editor(course_df, num_rows="dynamic", key="course_edit")

if st.button("💾 Save Changes to CSV"):
    save_data(edited_summary, edited_rounds, edited_course)
    st.success("Data saved successfully!")
