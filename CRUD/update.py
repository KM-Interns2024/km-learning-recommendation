from pinecone import Pinecone
from tkinter import messagebox
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


def update_vector_positions(id, value1, value2):
    if((float(value1) >= 0 and float(value1) <= 1) and (float(value2) >= 0 and float(value2) <= 1)):
        index = pc.Index(index_name)
        list = []

        list = [value1, value2]

        index.update(id, list, namespace="positions")
        return index
    else:
        messagebox.showerror("Wrong Value, please enter a value between 0 and 1")

def update_vector_metadata_employees(id, value1, value2, metadata):
    if((float(value1) >= 0 and float(value1) <= 1) and (float(value2) >= 0 and float(value2) <= 1)):
        index = pc.Index(index_name)

        list = [value1, value2]

        index.update(id, list, {f"Position": metadata}, namespace="employees")
        return index
    else:
        messagebox.showerror("Wrong Value, please enter a value between 0 and 1")

def update_vector_metadata_courses(id, value1, value2, metadata1, metadata2):
    if((float(value1) >= 0 and float(value1) <= 1) and (float(value2) >= 0 and float(value2) <= 1)):
        index = pc.Index(index_name)

        list = [value1, value2]

        index.update(id, list, {f"Category": metadata1, "Technology": metadata2}, namespace="courses")
        return index
    else:
        messagebox.showerror("Wrong Value, please enter a value between 0 and 1")
