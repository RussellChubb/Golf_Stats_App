# To Do
# - The Main plot should be a bar graph. Ideally, we should have some filters where you can only select one "type" at a time, because otherwise we're plotting practice rounds, full 18 etc on the same axis.
# - We need to make make the metrics look better, I'll paste some code below for how to style them.
'''
metric_style = (
    "background-color:rgba(38,39,48,0.7);"
    "border:2px solid rgba(125,90,188,0.7); # Make this green tho"
    "border-radius:10px;"
    "padding:1em 0.5em;"
    "text-align:center;"
    "margin-bottom:0.5em;"
)
'''
# - We Also need a favicon for the pages
# - The home page needs to have an icon on the tab too
# - I would like to have pages on the sidebar sit within other pages by category. So for example, the analysis pages (like this one) would sit under an "Analysis" category on the sidebar.
# - The graph needs to have titles in white



# Imports
import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.metrics import get_summary_stats
from utils.visuals import plot_score_trend

# Page Configuration
st.set_page_config(
    page_title="Golf Tracker",
    page_icon="⛳",
    layout="wide"
)

# Custom CSS for metrics
st.markdown("""
<style>
.metric-container {
    background-color: rgba(38,39,48,0.7);
    border: 2px solid rgba(46,204,113,0.7);
    border-radius: 10px;
    padding: 1em 0.5em;
    text-align: center;
    margin-bottom: 0.5em;
}
</style>
""", unsafe_allow_html=True)

# Page Title & Sub Title
st.title("⛳ Golf Performance Dashboard")
st.subheader("Track and analyze your golf game over time")

# Load data
summary_df, rounds_df, course_df = load_data()

# Visual divider
st.divider()

# Summary cards with custom styling
stats = get_summary_stats(summary_df)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric("Best Score", stats["best_score"], stats["best_course"])
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric("Average Score", stats["avg_score"])
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric("Avg vs Par", f"{stats['avg_diff']:+}")
    st.markdown('</div>', unsafe_allow_html=True)

# Visual Divider
st.divider()

st.subheader("📈 Score Trend Over Time")
round_types = ['All'] + list(summary_df['Type'].unique())
selected_type = st.selectbox('Select Round Type:', round_types)

# Filter data based on selection
if selected_type != 'All':
    fig = plot_score_trend(summary_df, selected_type)
else:
    fig = plot_score_trend(summary_df)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🏌️ Recent Rounds")
st.dataframe(summary_df.sort_values("Date", ascending=False).head(5))
