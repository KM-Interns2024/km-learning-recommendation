from pinecone import Pinecone
import numpy as np

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
index = pc.Index("kbc")

def query_vector(namespace):
    vector_input = input("What vectors would you like to query? ")
    vector = list(map(float, vector_input.split(',')))

    results = index.query(
        namespace=namespace,
        vector=vector,
        top_k=3,
        include_values=True
    )

    return results

def query_id(namespace):
    vector_id = input("What is the ID of the vector you would like to query? ")
    results = index.query(
        namespace=namespace,
        id=vector_id,
        top_k=1,
        include_values=True
    ).get("matches")

    return results[0].get("values")

def query_vector_id_courses():
    index = pc.Index("courses")
    vector_id = input("What vectors would you like to query? ")
    
    results = index.fetch([vector_id]).get('vectors')
    
    values = results['Deep_Learning_Specialization_492875_3']['values']
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

# print("Query results:", query_vector_id_courses())
# print("Query results:", query_vector())
# print("Query results:", query_id(input("What is the position? ")))
# print("Query results: ", query_course_rec)