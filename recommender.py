# K-Means Clustering
import sys
import os
# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from CRUD.read import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

def recommender(position):
    # Querying the data from Pinecone
    data_list = query_all_positions()

    # Encoding the string data to numerical data
    labelencoder_position = LabelEncoder()
    encoded_positions = labelencoder_position.fit_transform(data_list)

    X = encoded_positions.reshape(-1, 1)

    # Using the elbow method to find the optimal number of clusters
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
        kmeans.fit(X)   # Training
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    # plt.show()  # Here we see that the optimal number of clusters in this dataset(and X values) is 5

    # Training the K-Means model on the dataset
    kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
    y_kmeans = kmeans.fit_predict(X)   # Training and creating independent variable

    # Create a DataFrame to store the positions and their clusters
    import pandas as pd
    dataset = pd.DataFrame({'Position': data_list, 'Cluster': y_kmeans})

    # Function to recommend courses based on the position
    def recommend_courses(position):
        # Check if the input value is in the LabelEncoder classes
        if position not in labelencoder_position.classes_:
            return None
        
        # Encode the input
        encoded_position = labelencoder_position.transform([position])[0]
        
        # Predict the cluster
        cluster = kmeans.predict([[encoded_position]])[0]
        
        # Recommend courses from the same cluster
        recommended_courses = dataset[dataset['Cluster'] == cluster]['Position']
        
        return recommended_courses.tolist()

    # Example user input (replace with actual user input code)
    user_position = position

    # Recommend courses for the user input
    recommended_courses = recommend_courses(user_position)
    if recommended_courses is None:
        print("None")
        return None
    else:
        recommended_courses_str = "\n".join(recommended_courses)
        print(f"Recommended courses for the position {user_position}:\n{recommended_courses_str}")
        return f"Recommended courses for the position {user_position}:\n{recommended_courses_str}"
