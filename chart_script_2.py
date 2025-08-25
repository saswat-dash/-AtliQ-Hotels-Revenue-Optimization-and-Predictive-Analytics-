import plotly.graph_objects as go
import plotly.io as pio

# Data for the chart
categories = ['Current Perf', 'Weekday Target', 'Industry Target', 'Combined Pot']
room_nights = [134590, 14227, 16584, 165401]

# Colors: blue for current, green for opportunities, gold for combined
colors = ['#5D878F', '#2E8B57', '#2E8B57', '#D2BA4C']

# Create bar chart
fig = go.Figure(data=[
    go.Bar(
        x=categories,
        y=room_nights,
        marker_color=colors,
        text=[f'{val/1000:.0f}k' for val in room_nights],
        textposition='outside',
        cliponaxis=False
    )
])

# Update layout
fig.update_layout(
    title='Room-Night Optimization Opportunities',
    xaxis_title='Opportunity Type',
    yaxis_title='Room-Nights',
)

# Format y-axis to show values in thousands
fig.update_yaxes(
    tickformat='.0f',
    ticksuffix='',
    tickvals=[0, 50000, 100000, 150000, 200000],
    ticktext=['0', '50k', '100k', '150k', '200k']
)

# Save the chart
fig.write_image('room_night_optimization.png')