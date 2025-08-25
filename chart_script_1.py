import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

# Create room data
room_data = [
    {"room_class": "Standard", "sample_rate": 9.1, "occupancy": 57.88},
    {"room_class": "Presidential", "sample_rate": 26.6, "occupancy": 59.22}
]

# Create revenue realization data
revenue_data = [
    {"booking_status": "Checked Out", "realization": 100},
    {"booking_status": "No Show", "realization": 100}, 
    {"booking_status": "Cancelled", "realization": 40}
]

df_room = pd.DataFrame(room_data)
df_revenue = pd.DataFrame(revenue_data)

# Create figure
fig = go.Figure()

# Add room rates bars (in $k)
fig.add_trace(go.Bar(
    name='Rate ($k)',
    x=df_room['room_class'],
    y=df_room['sample_rate'],
    marker_color='#1FB8CD',
    yaxis='y',
    offsetgroup=1
))

# Add occupancy rates bars
fig.add_trace(go.Bar(
    name='Occupancy (%)', 
    x=df_room['room_class'],
    y=df_room['occupancy'],
    marker_color='#DB4545',
    yaxis='y2',
    offsetgroup=2
))

# Add revenue realization bars
fig.add_trace(go.Bar(
    name='Revenue Real (%)',
    x=df_revenue['booking_status'],
    y=df_revenue['realization'],
    marker_color='#2E8B57',
    yaxis='y2',
    offsetgroup=3
))

# Update layout with dual y-axes
fig.update_layout(
    title='Room Rates, Occupancy & Revenue',
    xaxis_title='Category',
    yaxis=dict(
        title='Rate ($k)',
        side='left'
    ),
    yaxis2=dict(
        title='Percentage (%)',
        side='right',
        overlaying='y'
    ),
    barmode='group',
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.05, 
        xanchor='center', 
        x=0.5
    )
)

# Save the chart
fig.write_image('room_revenue_chart.png')