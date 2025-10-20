# Example for tracking photon counts by plant and day

plants = { 'marigold': {'Day1': 99, 'Day2': 123},
           'golden rod':{'Day1': 103, 'Day2':137}}
# Check for Day3 photon counts, default to 0
for plant, readings in plants.items():
     day3 = readings.get ('Day3, 0')
     print(f"{plant} Day3 photon count: {day3}")