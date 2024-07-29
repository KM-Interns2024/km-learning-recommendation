from pinecone import Pinecone
import numpy as np
from misc.api_key import api_key

pc = Pinecone(api_key=api_key)

def query_id(index_name, namespace, vector_id):
    index = pc.Index(index_name)
    results = index.query(
        namespace=namespace,
        id=vector_id,
        top_k=1,
        include_values=True
    ).get('matches')

    return results[0].get('values')

def query_vector_id(index_name, vector_id):
    index = pc.Index(index_name)
    results = index.query(
        namespace="employees",
        id=vector_id,
        top_k=3,
        include_values=True
    ).get('matches')

    return results


def get_vector_values_by_id(index_name, id):
    index = pc.Index(index_name)
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

    list = []
    for result in results:
        list.append(result.get('id'))

    return list