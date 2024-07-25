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
    namespace = input("Please enter a namespace to be truncated: ")
    try:
        index.delete(delete_all=True, namespace=namespace)
        print("All entries deleted successfully.")
    except Exception as e:
        print(f"Failed to delete entries: {e}")

def delete_vector_by_id():
    namespace = input("Enter a namespace you want to delete from: ")
    entry_id = input("Enter the ID of the entry you want to delete: ")
    index.delete(ids=[entry_id], namespace=namespace)
    print(f"Entry with ID '{entry_id}' has been deleted.")

def update_vector():
    index_name = input("Enter the name of the index: ")
    namespace = input("Enter the namespace of the desired entry to update: ")
    id = input("Enter the vector id you want to update: ")
    dimension = pc.describe_index(index_name).get('dimension')
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

def query_course_rec(vector, metadata):
    index = pc.Index("courses")
    results = index.query(
        vector=vector,
        filter={"Technology": metadata},
        top_k=5,
        include_values=True
    ).get("matches")

    lista = []
    for result in results:
        lista.append(result.get('id'))

    return lista

def query_vector_id_courses():
    index = pc.Index("courses")
    vector_id = input("What vectors would you like to query? ")
    
    results = index.fetch([vector_id]).get('vectors')
    
    values = results['Deep_Learning_Specialization_492875_3']['values']
    return values