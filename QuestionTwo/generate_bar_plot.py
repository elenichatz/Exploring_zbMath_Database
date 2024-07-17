import matplotlib.pyplot as plt
import numpy as np

# Data: Counts for each category from 2019 to 2023
categories = ['Deep Learning\nand Neural Networks', 'Machine Learning\nand Reinforcement Learning', 
              'Optimization\nand Control', 'Statistics', 'Mathematics\nand Theoretical\nComputer Science']

# Counts per category over the years 2019-2023
counts = [
    {'year': 2019, 'counts': [61, 0, 45, 38, 95]},
    {'year': 2020, 'counts': [37, 54, 11, 1, 108]},
    {'year': 2021, 'counts': [34, 56, 10, 2, 128]},
    {'year': 2022, 'counts': [17, 34, 9, 1, 118]},
    {'year': 2023, 'counts': [22, 45, 4, 2, 129]}
]

# Extracting years and counts
years = [data['year'] for data in counts]
yearly_counts = {category: [data['counts'][i] for data in counts] for i, category in enumerate(categories)}

# Define bar width
bar_width = 0.1
bar_positions = np.arange(len(years))

# Define a colormap for categories
colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))

# Plotting
plt.figure(figsize=(14, 8))

# Loop through categories and plot bar chart with specified colors
for i, category in enumerate(categories):
    plt.bar(bar_positions + i * bar_width, yearly_counts[category], bar_width, label=category, color=colors[i])

plt.xlabel('Year')
plt.ylabel('Counts')
plt.title('Distribution of Research Topics by Category (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(bar_positions + bar_width * (len(categories) / 2), years)
plt.tight_layout()

# Display the plot
plt.show()
