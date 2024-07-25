from pinecone import Pinecone
import numpy as np
from misc.api_key import api_key


pc = Pinecone(api_key=api_key)
index = pc.Index("kbc")

skills = ["Python", "Java", "C++", "C", "C#", "JavaScript", "Ruby", 
          "PHP", "Swift", "Objective-C", "R", "Perl", "Scala", "Go", "HTML", "CSS"]




def query_id(namespace):
    vector_id = input("What is the ID of the vector you would like to query? ")
    results = index.query(
        namespace=namespace,
        id=vector_id,
        top_k=1,
        include_values=True
    ).get("matches")

    return results[0].get("values")

def query_vector_id(vector_id):
    results = index.query(
        namespace="employees",
        id=vector_id,
        top_k=3,
        include_values=True
    ).get('matches')

    return results

def delete_all():
    namespace = "employees"
    try:
        index.delete(delete_all=True, namespace=namespace)
        print("All entries deleted successfully.")
    except Exception as e:
        print(f"Failed to delete entries: {e}")

def delete_vector_by_id():
    namespace = "employees"
    entry_id = input("Enter the ID of the entry you want to delete: ")
    index.delete(ids=[entry_id], namespace=namespace)
    print(f"Entry with ID '{entry_id}' has been deleted.")

def update_vector():

    namespace = input("Enter your namespace: ")
    id = input("Enter the vector id you want to update: ")
    dimension = pc.describe_index('kbc').get('dimension')
    list = []

    for el in range(dimension):
        temp = float(input(f"Please enter a value for {skills[el]}: "))
        while(temp < 0 or temp > 1):
            temp = float(input(f"Please enter a value between 0.0 and 1.0 for {skills[el]} : "))
        list.append(temp)
    
    index.update(id, list, namespace=namespace)
    return list

def get_vector_values_by_id(id):
    result = index.fetch([f'{id}']).get('values')
    values = result[id]['values']
    return values