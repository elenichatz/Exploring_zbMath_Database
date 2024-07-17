import matplotlib.pyplot as plt
import numpy as np

# Data: Counts for each category from 2019 to 2023
categories = [
    'Deep Learning\nand Neural Networks', 
    'Machine Learning\nand Reinforcement Learning', 
    'Optimization\nand Control', 
    'Statistics', 
    'Mathematics\nand Theoretical\nComputer Science'
]

# Counts per category over the years 2019-2023
counts = [
    {'year': 2019, 'counts': [61, 0, 45, 38, 95]},
    {'year': 2020, 'counts': [37, 54, 11, 1, 108]},
    {'year': 2021, 'counts': [34, 56, 10, 2, 128]},
    {'year': 2022, 'counts': [17, 34, 9, 1, 118]},
    {'year': 2023, 'counts': [22, 45, 4, 2, 129]}
]

# Extracting counts for each year
yearly_counts = {category: [data['counts'][i] for data in counts] for i, category in enumerate(categories)}

# Years list for x-axis
years = [data['year'] for data in counts]

# Colors for each category
colors = ['blue', 'green', 'orange', 'red', 'purple']

# Plotting
plt.figure(figsize=(12, 8))

# Loop through categories and plot bubble chart
for i, category in enumerate(categories):
    sizes = yearly_counts[category]
    plt.scatter(years, np.repeat(i, len(years)), s=[size * 5 for size in sizes], 
                c=colors[i], label=category, edgecolors='black', linewidth=1.5)

plt.yticks(np.arange(len(categories)), categories)
plt.xticks(years)  # Ensuring only the years 2019-2023 are displayed on x-axis
plt.xlabel('Year')
plt.title('Distribution of Research Topics by Category (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
