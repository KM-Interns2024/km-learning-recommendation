# K-Means Clustering
import sys
import os
import random

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from CRUD.read import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path


def recommender(position):
    # Query the courses and positions
    course_ids, recommended_for = query_courses()

    # Initialize LabelEncoder for both course_ids and recommended_for
    labelencoder_course = LabelEncoder()
    labelencoder_position = LabelEncoder()

    # Encode the course_ids and recommended_for positions
    encoded_course_ids = labelencoder_course.fit_transform(course_ids)
    encoded_positions = labelencoder_position.fit_transform(recommended_for)

    # Combine encoded course IDs and encoded positions into a single variable X
    X = np.array(list(zip(encoded_course_ids, encoded_positions)))

    # Using the elbow method to find the optimal number of clusters
    # wcss = []
    # for i in range(1, 11):
    #     kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    #     kmeans.fit(X)   # Training
    #     wcss.append(kmeans.inertia_)
    # plt.plot(range(1, 11), wcss)
    # plt.title('The Elbow Method')
    # plt.xlabel('Number of clusters')
    # plt.ylabel('WCSS')
    # plt.show()  # Display the plot

    # Training the K-Means model on the dataset
    kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
    y_kmeans = kmeans.fit_predict(X)  # Training and creating cluster assignments

    # Create a DataFrame to store the courses, positions, and their clusters
    dataset = pd.DataFrame({'CourseID': course_ids, 'Position': recommended_for, 'Cluster': y_kmeans})

    # Function to recommend courses based on the position
    def recommend_courses(position):
        # Check if the input value is in the LabelEncoder classes
        if position not in labelencoder_position.classes_:
            return None

        # Encode the input
        encoded_position = labelencoder_position.transform([position])[0]

        # Predict the cluster for the given position
        cluster = dataset['Cluster'].unique()

        # Recommend courses from the same cluster
        selected_cluster = random.choice(cluster)
        recommended_courses = dataset[dataset['Cluster'] == selected_cluster]['CourseID']

        return recommended_courses.tolist()

    # Example user input (replace with actual user input code)
    user_position = position  # Replace with actual user input

    # Recommend courses for the user input
    recommended_courses = recommend_courses(user_position)
    if recommended_courses is None:
        print("None")
    else:
        recommended_courses_str = "\n".join(recommended_courses)
        print(f"Position:\n{user_position}\n\nRecommended Courses:\n{recommended_courses_str}")
        return f"Position:\n{user_position}\n\nRecommended Courses:\n{recommended_courses_str}"
