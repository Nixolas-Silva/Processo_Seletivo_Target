import xml.etree.ElementTree as ET
from collections import defaultdict

# Parse the XML file
tree = ET.parse('dados2.xml')
root = tree.getroot()

# Create dictionaries to store the highest and lowest values for each day,
# as well as the daily values and the number of measurements for each day
values = defaultdict(lambda: {'min': float('inf'), 'max': float('-inf'), 'daily': [], 'count': 0})

# Iterate over each measurement in the XML file
for measurement in root.findall('.//medicao'):
    # Get the date and value from the measurement
    day = measurement.find('dia').text
    value = measurement.find('valor').text
    if value:
        value = float(value)
        # Check if the value is higher or lower than the current minimum or maximum
        if value < values[day]['min']:
            values[day]['min'] = value
        if value > values[day]['max']:
            values[day]['max'] = value

        # Add the value to the daily values list and increment the count
        values[day]['daily'].append(value)
        values[day]['count'] += 1

# Calculate the daily average and count the number of days where the daily
# value was higher than the daily average
daily_sum = 0
daily_count = 0
num_higher = 0

for day in values:
    if values[day]['count'] > 0:
        # Calculate the daily average
        daily_average = sum(values[day]['daily']) / values[day]['count']
        daily_sum += daily_average
        daily_count += 1

        # Count the number of days where the daily value was higher than the daily average
        for value in values[day]['daily']:
            if value > daily_average:
                num_higher += 1

# Print the results
print(f"Highest and lowest values for each day:")
for day in values:
    if values[day]['count'] > 0:
        print(f"Day {day}: highest = {values[day]['max']}, lowest = {values[day]['min']}")
print(f"\nNumber of days where the daily value was higher than the daily average: {num_higher}")
