from pinecone import Pinecone
import numpy as np

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
index = pc.Index("kbc")

def query_vector(vector):
    vector_input = vector
    vector = list(map(float, vector_input.split(',')))

    results = index.query(
        namespace="",
        vector=vector,
        top_k=3,
        include_values=True
    )

    return results

def query_id(vector_id):
    results = index.query(
        namespace="",
        id=vector_id,
        top_k=3,
        include_values=True
    )

    return results

print("Query results:", query_vector(input("What vectors would you like to query? ")))
print("Query results:", query_id(input("What is the ID of the vector you would like to query? ")))
