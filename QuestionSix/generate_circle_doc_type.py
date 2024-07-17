import matplotlib.pyplot as plt
import numpy as np

# Data: Counts for each category from 2019 to 2023
categories = ['Journal article', 'Book', 'Serial article']

# Counts per category over the years 2019-2023
counts = [
    {'year': 2019, 'counts': [83, 2, 10]},
    {'year': 2020, 'counts': [85, 7, 9]},
    {'year': 2021, 'counts': [80, 3, 4]},
    {'year': 2022, 'counts': [74, 7, 8]},
    {'year': 2023, 'counts': [74, 6, 11]}
]

# Extracting counts for each year
yearly_counts = {category: [data['counts'][i] for data in counts] for i, category in enumerate(categories)}

# Years list for x-axis
years = [data['year'] for data in counts]

# Colors for each category
colors = ['blue', 'green', 'orange']

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
plt.title('Distribution of The Documentation Types (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()