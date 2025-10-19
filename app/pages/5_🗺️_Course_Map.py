import streamlit as st
import pandas as pd
import pydeck as pdk
from utils.data_loader import load_user_data

st.title("🗺️ Course Map")

_, _, course_df = load_user_data()

# Ensure coordinates exist
if not {"Lat", "Lon"}.issubset(course_df.columns):
    st.warning("No GPS coordinates found in Course Data (columns 'Lat' and 'Lon' missing).")
else:
    selected_course = st.selectbox("Select Course", course_df["Course"].unique())
    filtered = course_df[course_df["Course"] == selected_course]

    st.map(filtered[["Lat", "Lon"]], size=50, color="#007bff")

    st.subheader(f"Hole Locations — {selected_course}")
    st.dataframe(filtered[["Hole", "Par", "Distance", "Lat", "Lon"]])

    # Optional: nicer PyDeck visualization
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/satellite-streets-v12",
        initial_view_state=pdk.ViewState(
            latitude=filtered["Lat"].mean(),
            longitude=filtered["Lon"].mean(),
            zoom=15,
            pitch=45
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=filtered,
                get_position='[Lon, Lat]',
                get_radius=8,
                get_color='[0, 100, 200, 180]',
                pickable=True
            ),
            pdk.Layer(
                "TextLayer",
                data=filtered,
                get_position='[Lon, Lat]',
                get_text='Hole',
                get_size=14,
                get_color='[255, 255, 255]',
                get_alignment_baseline='"bottom"'
            )
        ]
    ))
