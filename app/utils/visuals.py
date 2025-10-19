import matplotlib.pyplot as plt
import pandas as pd

def plot_score_trend(summary_df: pd.DataFrame):
    """Simple score-over-time chart."""
    df = summary_df.sort_values("Date")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Score"], marker="o", linestyle="-")
    ax.set_xlabel("Date")
    ax.set_ylabel("Score")
    ax.set_title("Scores Over Time")
    ax.grid(True)
    plt.xticks(rotation=45)
    return fig
