import plotly.graph_objects as go
import pandas as pd

# Since multi-panel dashboards with subplots are not allowed, 
# I'll create the most comprehensive single chart: City Performance with benchmark comparison

# City performance data
cities = ['Delhi', 'Hyderabad', 'Mumbai', 'Bangalore']
occupancy = [60.6, 58.1, 57.9, 55.8]

# Color coding: Green for good performance (above 60%), Blue for neutral (57-60%), Red for needs attention (below 57%)
colors = ['#2E8B57',  # Delhi - Green (city leader, above 60%)
          '#1FB8CD',  # Hyderabad - Blue (growth potential, 58-60%)
          '#5D878F',  # Mumbai - Blue (optimization target, 57-60%)
          '#DB4545'] # Bangalore - Red (intervention required, below 57%)

# Create the bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    x=cities,
    y=occupancy,
    marker_color=colors,
    text=[f"{val:.1f}%" for val in occupancy],
    textposition='outside',
    cliponaxis=False,
    name='City Occupancy'
))

# Add industry benchmark line at 65%
fig.add_hline(y=65, line_dash="dash", line_color="gray", 
              annotation_text="Industry: 65%", annotation_position="top right")

# Add overall performance line at 57.9%
fig.add_hline(y=57.9, line_dash="dot", line_color="orange", 
              annotation_text="Overall: 57.9%", annotation_position="bottom right")

# Update layout
fig.update_layout(
    title='City Performance vs Benchmarks',
    xaxis_title='Cities',
    yaxis_title='Occupancy %',
    showlegend=False
)

# Update y-axis to show percentage format with appropriate range
fig.update_yaxes(
    tickformat='.0f',
    ticksuffix='%',
    range=[50, 70]
)

# Save the chart
fig.write_image('city_performance_vs_benchmarks.png')