import matplotlib.pyplot as plt
import numpy as np

# Data: Counts for each category from 2019 to 2023
categories = ['English', 'Chinese', 'Catalan' ] 
# Counts per category over the years 2019-2023
counts = [
    {'year': 2019, 'counts': [89, 1, 0]},
    {'year': 2020, 'counts': [93, 1, 0]},
    {'year': 2021, 'counts': [93, 0, 1]},
    {'year': 2022, 'counts': [82, 0, 0]},
    {'year': 2023, 'counts': [85, 0, 0]}
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
plt.title('Distribution of Languages Of Documentations (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(bar_positions + bar_width * (len(categories) / 2), years)
plt.tight_layout()

# Display the plot
plt.show()