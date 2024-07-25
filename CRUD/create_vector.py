import csv
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
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

# Insert employees vectors into Pinecone index
def insert_employees():
    for i, vector in enumerate(employees):
        vector_id = add_name_id(f"../employees.csv", i)
        print(f"Person {vector_id}")
        # Create a Pinecone index
        index_name = 'kbc'
        index = pc.Index(index_name)
        current_vector = [float(element) for element in vector]

        # Correctly insert vectors into Pinecone index using the index object
        if vector_id is not None:
            try:
                index.upsert([(vector_id, current_vector)],namespace="employees")
                print(f"Successfully inserted vector for '{vector_id}' into '{index_name}' index.")
            except Exception as e:
                print(f"Vector insertion failed for '{vector_id}': {e}")
        else:
            print(f"No name found for vector at index {i+1}; vector not inserted.")

# Insert positions vectors into Pinecone index
def insert_positions():
    for i, vector in enumerate(positions):
        vector_id = add_name_id("../positions.csv", i)
        print(f"Position {vector_id}")
        # Create a Pinecone index
        index_name = 'kbc'
        index = pc.Index(index_name)
        current_vector = [float(element) for element in vector]

        # Correctly insert vectors into Pinecone index using the index object
        if vector_id is not None:
            try:
                index.upsert([(vector_id, current_vector)],namespace="positions")
                print(f"Successfully inserted vector for '{vector_id}' into '{index_name}' index.")
            except Exception as e:
                print(f"Vector insertion failed for '{vector_id}': {e}")
        else:
            print(f"No name found for vector at index {i+1}; vector not inserted.")

def add_metadata():
    csvfile = "../courses.csv"
    with open(csvfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        technologies = reader.fieldnames[5:]  # Assuming skills start from the 4th column
        metadata_list = []
        for row in reader:
            # Convert to dictionary
            technologies_dict = {tech: row[tech] for tech in technologies}
            metadata_list.append(technologies_dict)
    return metadata_list


def vectorise_courses():
    csvfile = "../courses.csv"
    with open(csvfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        skills = reader.fieldnames[4:5]  # Assuming skills start from the 4th column
        vectors = []
        for row in reader:
            skills_vector = [float(row[skill]) for skill in skills]
            vectors.append(skills_vector)
    return vectors

# Insert courses vectors into Pinecone index
def insert_courses():
    vector = vectorise_courses()
    metadata_list = add_metadata()
    for i, vector in enumerate(vector):
        vector_id = add_name_id("../courses.csv", i)
        metadata = metadata_list[i]
        print(f"Course {vector_id}")
        # Create a Pinecone index
        index_name = 'courses'
        index = pc.Index(index_name)
        current_vector = [float(element) for element in vector]

        # Correctly insert vectors into Pinecone index using the index object
        if vector_id is not None:
            try:
                index.upsert([(vector_id, current_vector, metadata)])
                print(f"Successfully inserted vector for '{vector_id}' into '{index_name}' index.")
            except Exception as e:
                print(f"Vector insertion failed for '{vector_id}': {e}")
        else:
            print(f"No name found for vector at index {i+1}; vector not inserted.")






csv_employees = '../employees.csv'
employees = vectorize_skills(csv_employees)

csv_positions = '../employees.csv'
positions = vectorize_skills(csv_positions)

# Create a Pinecone index
if 'kbc' not in pc.list_indexes().names():
    pc.create_index(
        name='kbc',
        dimension=16,
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# Create a Pinecone index
if 'courses' not in pc.list_indexes().names():
    pc.create_index(
        name='courses',
        dimension=1,
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# insert_employees()
# insert_positions()
insert_courses()
