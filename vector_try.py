import os
import csv
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
index = pc.Index("vectortry")

skills = ["Python", "Java", "C++", "C", "C#", "JavaScript", "Ruby", "PHP", "Swift", "Objective-C", "R", "Perl", "Scala", "Go", "HTML", "CSS"]

def vectorize_skills(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        skills = reader.fieldnames[3:]  # Assuming skills start from the 4th column
        vectors = []
        for row in reader:
            person_vector = [float(row[skill]) for skill in skills]
            vectors.append(person_vector)
    return vectors

csv_file = 'job_positions_skills.csv'  # Replace with the actual path to your CSV file
vectors = vectorize_skills(csv_file)



if 'vectortry' not in pc.list_indexes().names():
    pc.create_index(
        name='vectortry',
        dimension=16,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

for i, vector in enumerate(vectors):
    print(f"Person {i+1} vector:", vector)
    # Create a Pinecone index
    index_name = 'vectortry'
    index = pc.Index(index_name)
    current_vector = [float(element) for element in vector]

    user_id = 'user123'
    index.upsert([(user_id, current_vector)])
    # Insert vectors into Pinecone index
    try:
        index.upsert([(user_id, current_vector)])
        Pinecone.upsert_items(index_name, vector)
        print(f"Successfully inserted {len(vector)} vectors into '{index_name}' index.")
    except Exception as e:
        print(f"Vector insertion failed: {e}")
# Convert all elements in current_vector to floats

# # Store the vectors

# import numpy as np

# def calculate_upskilling_direction(current_vector, desired_vector):
#     return np.array(desired_vector) - np.array(current_vector)

# upskill_direction = calculate_upskilling_direction(current_vector, desired_vector)

# # Assume the user has improved their skills
# current_skills = developer_3_desired_skills
# current_vector = vectorize_skills(current_skills)

# # Update the vector in Pinecone
# index.upsert([(user_id, current_vector)])

