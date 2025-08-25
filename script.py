# Recreate the comprehensive analysis with the corrected approach
import pandas as pd
import numpy as np
from datetime import datetime

# Recreate the core analysis data that we established earlier
print("=== FINAL ATLIQ HOTELS ANALYSIS - ALL DELIVERABLES ===")

# Core performance metrics (validated from our analysis)
core_metrics = {
    'overall_occupancy': 57.9,
    'weekend_occupancy': 73.6,
    'weekday_occupancy': 51.3,
    'weekend_weekday_gap': 22.2,
    'total_properties': 25,
    'total_bookings': 134590,
    'total_capacity': 232576,
    'analysis_days': 92
}

# City performance data
city_performance = pd.DataFrame({
    'city': ['Delhi', 'Hyderabad', 'Mumbai', 'Bangalore'],
    'occupancy_rate': [60.55, 58.07, 57.88, 55.77],
    'successful_bookings': [24231, 34888, 43455, 32016],
    'capacity': [40020, 60076, 75072, 57408]
})

# Room class performance
room_performance = pd.DataFrame({
    'room_class': ['Presidential', 'Standard', 'Elite', 'Premium'],
    'occupancy_rate': [59.22, 57.88, 57.61, 57.58],
    'successful_bookings': [16073, 38446, 49505, 30566],
    'capacity': [27140, 66424, 85928, 53084]
})

# Monthly trends
monthly_trends = pd.DataFrame({
    'month_year': ['May 2022', 'June 2022', 'July 2022'],
    'occupancy_rate': [58.55, 57.60, 57.45],
    'successful_bookings': [45882, 43683, 45025],
    'capacity': [78368, 75840, 78368]
})

# Top performing properties
top_properties = pd.DataFrame({
    'property_name': ['Atliq Palace', 'Atliq Blu', 'Atliq Palace', 'Atliq City', 'Atliq Exotica'],
    'city': ['Delhi', 'Mumbai', 'Mumbai', 'Hyderabad', 'Mumbai'],
    'occupancy_rate': [66.40, 66.28, 66.23, 66.19, 66.00],
    'category': ['Business', 'Luxury', 'Business', 'Business', 'Luxury']
})

# Bottom performing properties
bottom_properties = pd.DataFrame({
    'property_name': ['Atliq Grands', 'Atliq Seasons', 'Atliq Exotica', 'Atliq Bay', 'Atliq Palace'],
    'city': ['Bangalore', 'Mumbai', 'Hyderabad', 'Mumbai', 'Hyderabad'],
    'occupancy_rate': [44.40, 44.62, 44.63, 44.84, 52.98],
    'category': ['Luxury', 'Business', 'Luxury', 'Luxury', 'Business']
})

# Revenue context (from available data snippets)
revenue_context = {
    'standard_room_sample_rate': 9100,  # RT1
    'presidential_room_sample_rate': 26600,  # RT4
    'cancellation_retention_rate': 0.4,  # 40% retained on cancellations
    'successful_booking_realization': 1.0,  # 100% on checked out/no show
    'platforms_with_cancellation_data': ['logtrip', 'others', 'makeyourtrip', 'direct offline']
}

print(f"✅ Core analysis data prepared")
print(f"✅ City performance: {len(city_performance)} cities")
print(f"✅ Room classes: {len(room_performance)} categories") 
print(f"✅ Monthly trends: {len(monthly_trends)} months")
print(f"✅ Property analysis: {len(top_properties)} top + {len(bottom_properties)} bottom properties")
print(f"✅ Revenue context: Sample rates and policies included")