from pinecone import Pinecone
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
def create_all():
    pc = Pinecone(api_key=api_key)
    index = pc.Index("kbc")

pc = Pinecone(api_key=api_key)
index = pc.Index("kbc")

def delete_all(namespace):
    try:
        index.delete(delete_all=True, namespace=namespace)
        print("All entries deleted successfully.")
    except Exception as e:
        print(f"Failed to delete entries: {e}")

def delete_vector_by_id(id, namespace):
    index.delete(ids=[id], namespace=namespace)
    print(f"Entry with ID '{id}' has been deleted.")
