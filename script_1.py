# Create all dashboard data files
print("=== CREATING DASHBOARD DATA FILES ===")

# 1. Executive Summary Metrics
executive_summary = pd.DataFrame({
    'Metric': [
        'Overall Occupancy Rate',
        'Weekend Occupancy Rate', 
        'Weekday Occupancy Rate',
        'Weekend-Weekday Gap',
        'Industry Benchmark Gap',
        'Total Properties',
        'Analysis Period',
        'Total Successful Bookings',
        'Total Room Capacity',
        'Lost Room-Nights (vs 65% benchmark)',
        'Weekday Optimization Potential',
        'Best Performing Property',
        'Worst Performing Property',
        'Property Performance Variance'
    ],
    'Value': [
        '57.9%',
        '73.6%',
        '51.3%', 
        '22.2 percentage points',
        '7.1 percentage points below 65%',
        '25 properties',
        'May-July 2022 (92 days)',
        '134,590 room-nights',
        '232,576 room-nights',
        '16,584 room-nights (3 months)',
        '14,227 room-nights potential',
        '66.4% (Atliq Palace Delhi)',
        '44.4% (Atliq Grands Bangalore)', 
        '22.0 percentage points'
    ],
    'Priority': [
        'Monitor',
        'Maintain',
        'Critical - Improve',
        'Primary Focus',
        'Industry Alignment',
        'Portfolio Scale',
        'Analysis Scope',
        'Volume Tracking',
        'Capacity Management',
        'Revenue Recovery',
        'Immediate Opportunity',
        'Best Practice Model',
        'Urgent Intervention',
        'Consistency Challenge'
    ]
})

# 2. City Performance Details
city_detailed = city_performance.copy()
city_detailed['market_position'] = ['Leader', 'Growth Potential', 'Optimization Target', 'Intervention Required']
city_detailed['strategic_priority'] = ['Maintain Excellence', 'Accelerate Growth', 'Improve Consistency', 'Market Focus']

# 3. Room Class Analysis
room_detailed = room_performance.copy()
room_detailed['revenue_tier'] = ['Premium', 'Volume', 'Mid-Tier', 'Mid-Tier']
room_detailed['sample_rate_observed'] = [26600, 9100, 'Not Available', 'Not Available']
room_detailed['strategic_focus'] = ['Capacity Expansion', 'Volume Optimization', 'Positioning Clarity', 'Value Proposition']

# 4. Weekly Performance Pattern
weekly_pattern = pd.DataFrame({
    'day_type': ['Weekday', 'Weekend'],
    'occupancy_rate': [51.3, 73.6],
    'capacity_share': [70.7, 29.3],  # Approximate based on 5 weekdays vs 2 weekend days
    'performance_vs_overall': [-6.6, 15.7],  # vs 57.9% overall
    'optimization_priority': ['High - 22.2pp gap', 'Maintain - Strong performance']
})

# 5. Revenue Context Summary (from available data snippets)
revenue_insights = pd.DataFrame({
    'Category': [
        'Room Class Pricing Hierarchy',
        'Standard Room Sample Rate',
        'Presidential Room Sample Rate', 
        'Price Ratio (Presidential vs Standard)',
        'Cancellation Revenue Retention',
        'Successful Booking Revenue Realization',
        'Platform Cancellation Policy Consistency',
        'Revenue Protection Effectiveness'
    ],
    'Value': [
        'RT1 < RT2 < RT3 < RT4',
        '$9,100 per booking',
        '$26,600 per booking',
        '2.9x premium pricing',
        '40% retained (0.4 ratio)',
        '100% realized (1.0 ratio)',
        'Uniform across platforms',
        'Strong policy implementation'
    ],
    'Source': [
        'Data snippet analysis',
        'fact_bookings.csv sample',
        'fact_bookings.csv sample',
        'Calculated from samples',
        'Platform analysis',
        'Platform analysis', 
        'Multi-platform validation',
        'Policy effectiveness assessment'
    ]
})

# Save all files
executive_summary.to_csv('executive_summary_final.csv', index=False)
city_detailed.to_csv('city_performance_detailed.csv', index=False)
room_detailed.to_csv('room_class_detailed.csv', index=False)
monthly_trends.to_csv('monthly_trends_final.csv', index=False)
top_properties.to_csv('top_properties_final.csv', index=False)
bottom_properties.to_csv('bottom_properties_final.csv', index=False)
weekly_pattern.to_csv('weekly_performance_pattern.csv', index=False)
revenue_insights.to_csv('revenue_context_insights.csv', index=False)

print("✅ Created executive_summary_final.csv - Key metrics dashboard")
print("✅ Created city_performance_detailed.csv - Geographic analysis")
print("✅ Created room_class_detailed.csv - Product mix insights")
print("✅ Created monthly_trends_final.csv - Temporal patterns")
print("✅ Created top_properties_final.csv - Best practice models")
print("✅ Created bottom_properties_final.csv - Intervention targets")
print("✅ Created weekly_performance_pattern.csv - Weekday vs weekend")
print("✅ Created revenue_context_insights.csv - Financial context")

print(f"\n📊 DASHBOARD FILES READY: 8 comprehensive data files created")