import streamlit as st
from utils.data_loader import load_user_data
import streamlit as st
import pandas as pd
import pydeck as pdk
from utils.data_loader import load_user_data
from streamlit_option_menu import option_menu

summary_df, rounds_df, course_df = load_user_data()

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

st.title("📊 Round Summary")

selected_round_date = st.selectbox(
    "Select Round Date", summary_df["Date"].dt.strftime("%Y-%m-%d").unique()
)
selected_course = summary_df.loc[
    summary_df["Date"].dt.strftime("%Y-%m-%d") == selected_round_date, "Course"
].values[0]

st.subheader(f"Round Details — {selected_course} ({selected_round_date})")

round_data = rounds_df[
    (rounds_df["Course"] == selected_course)
    & (rounds_df["Date"].dt.strftime("%Y-%m-%d") == selected_round_date)
]
st.dataframe(round_data[["Hole", "Score"]])

_, course_df = load_user_data()

# Ensure coordinates exist
if not {"Lat", "Lon"}.issubset(course_df.columns):
    st.warning(
        "No GPS coordinates found in Course Data (columns 'Lat' and 'Lon' missing)."
    )
else:
    selected_course = st.selectbox("Select Course", course_df["Course"].unique())
    filtered = course_df[course_df["Course"] == selected_course]

    st.map(filtered[["Lat", "Lon"]], size=50, color="#007bff")

    st.subheader(f"Hole Locations — {selected_course}")
    st.dataframe(filtered[["Hole", "Par", "Distance", "Lat", "Lon"]])

    # Optional: nicer PyDeck visualization
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/satellite-streets-v12",
            initial_view_state=pdk.ViewState(
                latitude=filtered["Lat"].mean(),
                longitude=filtered["Lon"].mean(),
                zoom=15,
                pitch=45,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=filtered,
                    get_position="[Lon, Lat]",
                    get_radius=8,
                    get_color="[0, 100, 200, 180]",
                    pickable=True,
                ),
                pdk.Layer(
                    "TextLayer",
                    data=filtered,
                    get_position="[Lon, Lat]",
                    get_text="Hole",
                    get_size=14,
                    get_color="[255, 255, 255]",
                    get_alignment_baseline='"bottom"',
                ),
            ],
        )
    )
