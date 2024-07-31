import sys
import os
import csv
from pinecone import Pinecone


# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from misc.api_key import api_key
finally:
    # Restore the original sys.path
    sys.path = original_sys_path
def create_all():
    pc = Pinecone(api_key=api_key)
    index = pc.Index("kbc")

    skills = ["Hard", "Soft"]
    def add_name_id(filename, index):
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for i, row in enumerate(csv_reader):
                if i == index:  # Match the row in the CSV to the current vector index
                    return row['Name'] + "_" + row['Level']
        return None  # Return None or a default value if no matching row is found

    # 
    # 
    # START: FOR KBC INDEX
    # 
    # 

    # Opens CSV and vectorises data employees&positions
    def kbc_vectorize_skills(csv_file):
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            skills = reader.fieldnames[3:5]  # Assuming skills start from the 4th column
            vectors = []
            for row in reader:
                skills_vector = [float(row[skill]) for skill in skills]
                vectors.append(skills_vector)
        return vectors

    # Insert employees&positions vectors into Pinecone index
    def kbc_insert(component, strName):
        for i, vector in enumerate(component):
            vector_id = add_name_id(f"../resources/{strName}.csv", i)
            print(f"{strName} {vector_id}")
            # Create a Pinecone index
            index_name = 'kbc'
            index = pc.Index(index_name)
            current_vector = [float(element) for element in vector]

            # Correctly insert vectors into Pinecone index using the index object
            if vector_id is not None:
                try:
                    index.upsert([(vector_id, current_vector)],namespace=f"{strName}")
                    print(f"Successfully inserted vector for '{vector_id}' into '{index_name}' index.")
                except Exception as e:
                    print(f"Vector insertion failed for '{vector_id}': {e}")
            else:
                print(f"No name found for vector at index {i+1}; vector not inserted.")

    # 
    # 
    # END: FOR KBC INDEX
    # 
    # 



    # 
    # 
    # START: FOR COURSES INDEX
    # 
    # 


    def add_metadata():
        csvfile = "../resources/courses.csv"
        with open(csvfile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            technologies = reader.fieldnames[5:]  # Assuming skills start from the 6th column
            metadata_list = []
            for row in reader:
                # Convert to dictionary
                technologies_dict = {tech: row[tech] for tech in technologies}
                metadata_list.append(technologies_dict)
        return metadata_list


    def vectorise_courses():
        csvfile = "../resources/courses.csv"
        with open(csvfile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            skills = reader.fieldnames[4:5]  # Assuming skills start from the 5th column
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
            vector_id = add_name_id("../resources/courses.csv", i)
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
                
    # 
    # 
    # END: FOR COURSES INDEX
    # 
    # 



    csv_employees = '../resources/employees.csv'
    employees = kbc_vectorize_skills(csv_employees)

    csv_positions = '../resources/positions.csv'
    positions = kbc_vectorize_skills(csv_positions)

    kbc_insert(employees, "employees")
    kbc_insert(positions, "positions")
    insert_courses()
