from pinecone import Pinecone
import numpy as np
from misc.api_key import api_key

pc = Pinecone(api_key=api_key)
index = pc.Index("kbc")

def delete_all(namespace):
    try:
        index.delete(delete_all=True, namespace=namespace)
        print("All entries deleted successfully.")
    except Exception as e:
        print(f"Failed to delete entries: {e}")

def delete_vector_by_id(namespace, id):
    namespace = input("Enter a namespace you want to delete from: ")
    index.delete(ids=[id], namespace=namespace)
    print(f"Entry with ID '{id}' has been deleted.")