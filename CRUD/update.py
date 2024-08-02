from pinecone import Pinecone
import numpy as np
import sys
import os

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

index_name = "kbc"
skills = ["Hard Skills", "Soft Skills"]


def update_vector(id, value1, value2, namespace):
    index = pc.Index(index_name)
    list = []

    list = list[value1, value2]
    
    index.update(id, list, namespace=namespace)
    return index

def update_vector_metadata(id, value1, value2, namespace, metadata):
    index = pc.Index(index_name)

    list = list[value1, value2]

    index.update(id, list, metadata, namespace=namespace)
    return index
