import matplotlib.pyplot as plt
import numpy as np

# Data: Counts for each category from 2019 to 2023
categories = [
'Algebra Fundamentals',
'Quadratic Equations and Functions',
'Differential Calculus Foundations',
'Differentiation and Derivatives',
'Matrix Multiplications and Transformations',
'Probability Basics'
'Sampling and Sampling Distributions'
]

# Counts per category over the years 2019-2023
counts = [
    {'year': 2019, 'counts': [0, 0, 1, 4, 12, 3, 4]},
    {'year': 2020, 'counts': [0, 0, 0, 3, 7, 10, 1]},
    {'year': 2021, 'counts': [6, 0, 4, 0, 11, 0, 9]},
    {'year': 2022, 'counts': [1, 3, 5, 0, 7, 0, 5]},
    {'year': 2023, 'counts': [1, 2, 3, 0, 5, 0, 7]}
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
plt.title('Distribution of Research Topics Categorized by Math Theories (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(bar_positions + bar_width * (len(categories) / 2), years)
plt.tight_layout()

# Display the plot
plt.show()
