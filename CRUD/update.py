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

skills = ["Hard Skills", "Soft Skills"]


def update_vector(index_name, namespace, id):
    index = pc.Index(index_name)
    dimension = pc.describe_index(index_name).get('dimension')
    list = []

    for el in range(dimension): # el stands for element
        temp = float(input(f"Please enter a value for {skills[el]}: "))
        while(temp < 0 or temp > 1):
            temp = float(input(f"Please enter a value between 0.0 and 1.0 for {skills[el]} : "))
        list.append(temp)
    
    index.update(id, list, namespace=namespace)
    return list
