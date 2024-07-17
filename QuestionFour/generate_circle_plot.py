import matplotlib.pyplot as plt
import numpy as np

# Data: Counts for each category from 2019 to 2023
categories = ['Computer science', 'Systems theory\ncontrol', 
              'Statistics', 'Operations research\nmathematical programming', 
              'Game theory\neconomics behavior science', 
              'Information and communication\ntheory circuits', 'Numerical analysis']

# Counts per category over the years 2019-2023
counts = [
    {'year': 2019, 'counts': [83, 13, 50, 38, 13, 0, 0]},
    {'year': 2020, 'counts': [81, 0, 42, 20, 0, 23, 0]},
    {'year': 2021, 'counts': [86, 18, 52, 23, 8, 10, 16]},
    {'year': 2022, 'counts': [71, 24, 44, 33, 9, 0, 19]},
    {'year': 2023, 'counts': [69, 25, 31, 22, 6, 7, 24]}
]

# Extracting counts for each year
yearly_counts = {category: [data['counts'][i] for data in counts] for i, category in enumerate(categories)}

# Years list for x-axis
years = [data['year'] for data in counts]

# Colors for each category
colors = ['blue', 'green', 'orange', 'red', 'purple', 'pink', 'yellow']

# Plotting
plt.figure(figsize=(12, 8))

# Loop through categories and plot bubble chart
for i, category in enumerate(categories):
    sizes = yearly_counts[category]
    plt.scatter(years, np.repeat(i, len(years)), s=[size * 10 for size in sizes], 
                c=colors[i], alpha=0.5, label=category, edgecolors='black', linewidth=1.5)

plt.yticks(np.arange(len(categories)), categories)
plt.xticks(years)  # Ensuring only the years 2019-2023 are displayed on x-axis
plt.xlabel('Year')
plt.title('Distribution of Research Topics by Category (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

