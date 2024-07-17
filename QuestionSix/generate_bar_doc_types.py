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
plt.title('Distribution of The Documentation Types (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(bar_positions + bar_width * (len(categories) / 2), years)
plt.tight_layout()

# Display the plot
plt.show()