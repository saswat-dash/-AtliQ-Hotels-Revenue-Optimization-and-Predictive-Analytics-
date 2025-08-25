import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# Create timeline data
base_date = datetime(2024, 1, 1)

# Define activities with their phases, start and end dates
activities = [
    # Immediate Actions (0-60 days)
    {"Task": "Weekday Demand", "Phase": "Immediate", "Start": base_date, "End": base_date + timedelta(days=60)},
    {"Task": "Property Audits", "Phase": "Immediate", "Start": base_date, "End": base_date + timedelta(days=45)},
    {"Task": "Dynamic Price", "Phase": "Immediate", "Start": base_date + timedelta(days=15), "End": base_date + timedelta(days=60)},
    
    # Medium-term (60-180 days)
    {"Task": "Market Optimize", "Phase": "Medium-term", "Start": base_date + timedelta(days=60), "End": base_date + timedelta(days=150)},
    {"Task": "Product Mix", "Phase": "Medium-term", "Start": base_date + timedelta(days=75), "End": base_date + timedelta(days=180)},
    {"Task": "Op Standards", "Phase": "Medium-term", "Start": base_date + timedelta(days=90), "End": base_date + timedelta(days=180)},
    
    # Long-term (180-365 days)
    {"Task": "Industry Bench", "Phase": "Long-term", "Start": base_date + timedelta(days=180), "End": base_date + timedelta(days=300)},
    {"Task": "Revenue System", "Phase": "Long-term", "Start": base_date + timedelta(days=200), "End": base_date + timedelta(days=350)},
    {"Task": "Portfolio Grow", "Phase": "Long-term", "Start": base_date + timedelta(days=250), "End": base_date + timedelta(days=365)}
]

df = pd.DataFrame(activities)

# Create colors mapping for phases
colors = {
    "Immediate": "#1FB8CD",      # Strong cyan
    "Medium-term": "#DB4545",    # Bright red  
    "Long-term": "#2E8B57"       # Sea green
}

# Create Gantt chart using timeline
fig = px.timeline(df, 
                  x_start="Start", 
                  x_end="End", 
                  y="Task", 
                  color="Phase",
                  color_discrete_map=colors,
                  title="12-Month Strategic Roadmap")

# Update layout
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Activities",
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update y-axis to show tasks in reverse order (top to bottom by phase)
fig.update_yaxes(categoryorder="total ascending")

# Update x-axis to show months
fig.update_xaxes(
    tickformat="%b %Y",
    dtick="M1"
)

# Save the chart
fig.write_image("strategic_roadmap.png")