import matplotlib.pyplot as plt
from func_keywords_years import fetch_total_documents_for_year_with_keywords

# Define keywords
keywords = "ti: Support Vector Machines | ti: Decision Trees | ti: Gradient Descent | ti: Deep Learning | ti: Convolutional Neural Networks | ti: Recurrent Neural Networks | ti: Long Short-Term Memory Networks | ti: Generative Adversarial Networks | ti: Reinforcement Learning | ti: Supervised Learning | ti: Unsupervised Learning | ti: Semi-supervised Learning | ti: Transfer Learning | ti: Feature Extraction | ti: Feature Selection | ti: Dimensionality Reduction | ti: Principal Component Analysis | ti: Clustering Algorithms | ti: K-Means Clustering | ti: Hierarchical Clustering | ti: Ensemble Methods | ti: Random Forests | ti: Boosting and AdaBoost | ti: Bagging | ti: Neural Network Optimization | ti: Hyperparameter Tuning | ti: Cross-Validation | ti: Loss Functions | ti: Regularization Techniques | ti: Overfitting and Underfitting | ti: Data Augmentation | ti: Natural Language Processing | ti: Computer Vision | ti: Bayesian Networks | ti: Markov Decision Processes | ti: Q-learning | ti: Evolutionary Algorithms | ti: Genetic Algorithms"

# Fetch document counts for each year
document_counts = {year: fetch_total_documents_for_year_with_keywords(year, keywords) for year in range(2019, 2024)}

# Extract years and counts for plotting
years = list(document_counts.keys())
counts = list(document_counts.values())

plt.figure(figsize=(10, 6))  # Adjust the size of the plot as needed
plt.plot(years, counts, marker='o', linestyle='-', color='b')  # Plot the data

# Adding titles and labels
plt.title('Number of Documents Published per Year with AI keywords in Title (2019-2023)')
plt.xlabel('Year')
plt.ylabel('Number of Documents')

# Set the x-ticks to integer years
plt.xticks(years)

# Optionally, add grid lines for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()  # Display the plot