import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

def plot_score_trend_interactive(df):
    """Create an interactive score trend plot using Plotly"""
    fig = px.line(
        df.sort_values('Date'),
        x='Date',
        y='Score',
        markers=True,
        title='Score History',
        hover_data=['Course', 'ScoreDiff']
    )
    
    # Add par line
    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['ParTotal'],
            name='Par',
            line=dict(dash='dash', color='rgba(0,0,0,0.3)')
        )
    )
    
    # Customize layout
    fig.update_layout(
        hovermode='x unified',
        xaxis_title='Date',
        yaxis_title='Score',
        showlegend=True,
        height=500
    )
    
    return fig

def plot_score_trend(df, round_type=None):
    """Create an interactive bar plot using Plotly"""
    # Filter by round type if specified
    if round_type:
        df = df[df['RoundType'] == round_type]
    
    fig = go.Figure()
    
    # Add bar chart for scores
    fig.add_trace(
        go.Bar(
            x=df['Date'],
            y=df['Score'],
            name='Score',
            hovertemplate='<b>Date:</b> %{x}<br>' +
                         '<b>Score:</b> %{y}<br>' +
                         '<b>Course:</b> %{customdata[0]}<br>' +
                         '<b>vs Par:</b> %{customdata[1]:+}<extra></extra>',
            customdata=df[['Course', 'ScoreDiff']].values
        )
    )
    
    # Add par line
    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['ParTotal'],
            name='Par',
            line=dict(dash='dash', color='rgba(255,255,255,0.3)')
        )
    )
    
    # Update layout for dark theme
    fig.update_layout(
        title={
            'text': 'Score History',
            'font': {'color': 'white'}
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            title='Date',
            titlefont={'color': 'white'},
            tickfont={'color': 'white'},
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=dict(
            title='Score',
            titlefont={'color': 'white'},
            tickfont={'color': 'white'},
            gridcolor='rgba(255,255,255,0.1)'
        ),
        legend=dict(font={'color': 'white'}),
        height=500
    )
    
    return fig
