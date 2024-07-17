import matplotlib.pyplot as plt

# Example data
data = {
    2023: 7,
    2022: 9,
    2021: 16,
    2020: 15,
    2019: 5
}

# Ensure the data is sorted by year
years = sorted(data.keys())
values = [data[year] for year in years]

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(years, values, color='skyblue')

# Add titles and labels
plt.title('Journalist with More than Two Publications by Year')
plt.xlabel('Year')
plt.ylabel('Journalist with More than Two Publications')

# Display the plot
plt.xticks(years)  # Ensure all years are displayed on the x-axis
plt.show()

