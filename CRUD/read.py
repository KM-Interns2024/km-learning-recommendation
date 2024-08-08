from pinecone import Pinecone
import os
import sys

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from misc.api_key import api_key
finally:
    # Restore the original sys.path
    sys.path = original_sys_path


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
        include_values=True,
        include_metadata=True
    ).get('matches')

    return results


def get_vector_values_by_id(id): # !!!
    index = pc.Index(index_name)
    result = index.fetch([f'{id}']).get('values')
    values = result['id']['values']

    return values


def query_all_positions():
    index = pc.Index(index_name)
    results = index.query(
        namespace='positions',
        vector=[0, 0],
        top_k=10000,
        include_values=True
    ).get("matches")

    list = []
    for result in results:
        list.append(result.get('id'))

    return list

def query_all(namespace):
    index = pc.Index(index_name)
    results = index.query(
        vector=[0, 0],
        namespace=namespace,
        top_k=10000,
        include_values=True,
        include_metadata=True
    ).get('matches')
    
    output = ""
    for result in results:
        if(namespace == 'positions'):
            list = result.get('id')
            output += f"ID: {list}\n\n"
        else:
            list = result.get('id')
            meta = result.get('metadata')
            output += f"ID: {list}\nMetadata: {', '.join(meta.values())}\n\n"    ###     REMEMBER!!!

    return output

def query_one(id, namespace):
    index = pc.Index(index_name)
    
    print(f"Querying with id: {id}, namespace: {namespace}")  # Debug print

    if namespace == 'positions':
        results = index.query(
            vector=query_id(namespace, id),  # This should be replaced with the actual vector if available
            namespace=namespace,
            top_k=1,
            include_values=True,
        ).get('matches')
    else:
        results = index.query(
            id=id,
            namespace=namespace,
            top_k=1,
            include_values=True,
            include_metadata=True
        ).get('matches')

    output = ""
    for result in results:
        if namespace == 'positions':
            list = result.get('id')
            vector = result.get('values')
            output += f"Vector: {vector}\n"
        else:
            list = result.get('id')
            vector = result.get('values')
            meta = result.get('metadata')
            output += f"Metadata:\n{', '.join(meta.values())}\nVector: {vector}\n"

    print(f"Query result: {output}")  # Debug print
    return output

def query_courses():
    index = pc.Index(index_name)
    results = index.query(
        vector=[0, 0],
        namespace='courses',
        top_k=10000,
        include_values=True,
        include_metadata=True
    ).get('matches')

    course_ids = []
    recommended_for = []

    for result in results:
        course_id = result.get('id')
        meta = result.get('metadata')
        recommended = meta.get('Recommended for')  # Extract "Recommended for" field
        course_ids.append(course_id)
        recommended_for.append(recommended)

    return course_ids, recommended_for

def get_list_of_ids(namespace):
    index = pc.Index(index_name)
    results = index.query(
        vector=[0, 0],
        namespace=namespace,
        top_k=10000,
        include_values=True,
        include_metadata=True
    ).get('matches')
    
    list = []
    for result in results:
        list.append(result.get('id'))
    
    return list