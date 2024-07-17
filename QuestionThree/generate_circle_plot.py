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

# Extracting counts for each year
yearly_counts = {category: [data['counts'][i] for data in counts] for i, category in enumerate(categories)}

# Years list for x-axis
years = [data['year'] for data in counts]

# Colors for each category
colors = ['blue', 'green', 'orange', 'red','purple', 'pink', 'black']

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
plt.title('Distribution of Research Topics Categorized by Math Theories (2019-2023)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
