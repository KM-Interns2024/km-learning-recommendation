import csv
from pinecone import Pinecone, ServerlessSpec
from misc.api_key import api_key

pc = Pinecone(api_key=api_key)
index = pc.Index("kbc")

skills = ["Python", "Java", "C++", "C", "C#", "JavaScript", "Ruby", "PHP", "Swift", "Objective-C", "R", "Perl", "Scala", "Go", "HTML", "CSS"]

def add_name_id(filename, index):
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for i, row in enumerate(csv_reader):
            if i == index:  # Match the row in the CSV to the current vector index
                return row['Name'] + "_" + row['Level']
    return None  # Return None or a default value if no matching row is found

# Opens CSV and vectorises data
def vectorize_skills(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        skills = reader.fieldnames[3:]  # Assuming skills start from the 4th column
        vectors = []
        for row in reader:
            skills_vector = [float(row[skill]) for skill in skills]
            vectors.append(skills_vector)
    return vectors

# Opens CSV and vectorises data
def vectorize_skills_courses(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        skills = reader.fieldnames[7:]  # Assuming skills start from the 8th column
        vectors = []
        for row in reader:
            skills_vector = [float(row[skill]) for skill in skills]
            vectors.append(skills_vector)
    return vectors


def create_index():
    if 'kbc' not in pc.list_indexes().names():
        pc.create_index(
            name='kbc',
            dimension=16,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )

csv_employees = 'resources/employees.csv'
employees_vectors = vectorize_skills(csv_employees)

csv_positions = 'resources/positions.csv'
positions_vectors = vectorize_skills(csv_positions)

csv_courses = 'resources/courses.csv'
courses_vectors = vectorize_skills_courses(csv_courses)
