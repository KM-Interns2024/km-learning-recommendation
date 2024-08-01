from pinecone import Pinecone
from misc.api_key import api_key

pc = Pinecone(api_key=api_key)
index_name = 'kbc'

def query_id(namespace, vector_id):
    index = pc.Index(index_name)
    results = index.query(
        namespace=namespace,
        id=vector_id,
        top_k=1,
        include_values=True
    ).get('matches')

    return results[0].get('values')


def query_vector_id(vector_id, namespace):
    index = pc.Index(index_name)
    results = index.query(
        namespace=namespace,
        id=vector_id,
        top_k=3,
        include_values=True
    ).get('matches')

    return results


def get_vector_values_by_id(id): # !!!
    index = pc.Index(index_name)
    result = index.fetch([f'{id}']).get('values')
    values = result[id]['values']

    return values


def query_course_rec(vector, metadata):
    index = pc.Index(index_name)
    results = index.query(
        vector=vector,
        top_k=5,
        include_values=True
    ).get("matches")

    list = []
    for result in results:
        list.append(result.get('id'))

    return list
