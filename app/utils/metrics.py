import pandas as pd

def get_summary_stats(summary_df: pd.DataFrame):
    """Compute high-level summary metrics."""
    best_row = summary_df.loc[summary_df["Score"].idxmin()]
    avg_score = summary_df["Score"].mean()
    avg_diff = summary_df["ScoreDiff"].mean()

    return {
        "best_score": int(best_row["Score"]),
        "best_course": best_row["Course"],
        "avg_score": round(avg_score, 1),
        "avg_diff": round(avg_diff, 1),
    }
