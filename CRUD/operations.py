from pinecone import Pinecone
import numpy as np


pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
index = pc.Index("kbc")

skills = ["Python", "Java", "C++", "C", "C#", "JavaScript", "Ruby", 
          "PHP", "Swift", "Objective-C", "R", "Perl", "Scala", "Go", "HTML", "CSS"]




def query_vector(vector):
    vector_input = vector
    vector = list(map(float, vector_input.split(',')))

    results = index.query(
        namespace="employees",
        vector=vector,
        top_k=3,
        include_values=True
    )

    return results

def query_vector_id(vector_id):
    results = index.query(
        namespace="employees",
        id=vector_id,
        top_k=3,
        include_values=True
    )

    return results

def delete_all():
    
    namespace = "employees"
    try:
        index.delete(delete_all=True, namespace=namespace)
        print("All entries deleted successfully.")
    except Exception as e:
        print(f"Failed to delete entries: {e}")

def delete_entry():
    namespace = "employees"
    entry_id = input("Enter the ID of the entry you want to delete: ")
    index.delete(ids=[entry_id], namespace=namespace)
    print(f"Entry with ID '{entry_id}' has been deleted.")

def vector_update():
    index_name = "kbc"
    index = pc.Index(index_name)
    namespace = input("Enter your namespace: ")
    id = input("Enter the vector id you want to update: ")
    dimension = pc.describe_index(str(index_name)).get('dimension')
    list = []

    for el in range(dimension):
        temp = float(input(f"Please enter a value for {skills[el]}: "))
        while(temp < 0 or temp > 1):
            temp = float(input(f"Please enter a value between 0.0 and 1.0 for {skills[el]} : "))
        list.append(temp)
    
    index.update(id, list, namespace=namespace)
    return list