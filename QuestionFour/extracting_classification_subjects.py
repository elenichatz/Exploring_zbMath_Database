import requests

def fetch_total_documents_for_year_with_keywords(year, keywords):
    base_url = "https://api.zbmath.org/v1/document/_search"
    formatted_list_keywords = f"({keywords})" # The list with the keywords 
    params = {
        "search_string": f"py: {year} & ( {formatted_list_keywords} )",
        "page": 0,
        "rpp": 100,  # Adjusted parameter name to 'rpp' as per API documentation
    }
    response = requests.get(base_url, params=params)
    return response

# Example usage
keywords = "ti: Support Vector Machines | ti: Decision Trees | ti: Gradient Descent | ti: Deep Learning | ti: Convolutional Neural Networks | ti: Recurrent Neural Networks | ti: Long Short-Term Memory Networks | ti: Generative Adversarial Networks | ti: Reinforcement Learning | ti: Supervised Learning | ti: Unsupervised Learning | ti: Semi-supervised Learning | ti: Transfer Learning | ti: Feature Extraction | ti: Feature Selection | ti: Dimensionality Reduction | ti: Principal Component Analysis | ti: Clustering Algorithms | ti: K-Means Clustering | ti: Hierarchical Clustering | ti: Ensemble Methods | ti: Random Forests | ti: Boosting and AdaBoost | ti: Bagging | ti: Neural Network Optimization | ti: Hyperparameter Tuning | ti: Cross-Validation | ti: Loss Functions | ti: Regularization Techniques | ti: Overfitting and Underfitting | ti: Data Augmentation | ti: Natural Language Processing | ti: Computer Vision | ti: Bayesian Networks | ti: Markov Decision Processes | ti: Q-learning | ti: Evolutionary Algorithms | ti: Genetic Algorithms"

year = 2023
response = fetch_total_documents_for_year_with_keywords(year,keywords)

# Check if the request was successful
if response.status_code == 200:
    json_response = response.json()  # Parse JSON response
    classification_subjects = []
    classification_codes = []
    for document in json_response.get('result', []):
        subjects = document.get('msc')
        for subject in subjects:
            classification_subjects.append(subject.get('text', []))
            classification_codes.append(subject.get('code', []))

    print(f"Classification subjects: {classification_subjects}")
    print(f"Classification codes: {classification_codes}")
else:
    print(f"Error fetching data. Status code: {response.status_code}")
