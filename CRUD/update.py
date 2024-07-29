from pinecone import Pinecone
import numpy as np
from misc.api_key import api_key

pc = Pinecone(api_key=api_key)

skills = ["Python", "Java", "C++", "C", "C#", "JavaScript", "Ruby", 
          "PHP", "Swift", "Objective-C", "R", "Perl", "Scala", "Go", "HTML", "CSS"]

#import skills in a separate file
def update_vector(index_name, namespace, id):
    index = pc.Index(index_name)
    dimension = pc.describe_index(index_name).get('dimension')
    list = []

    for el in range(dimension):
        temp = float(input(f"Please enter a value for {skills[el]}: "))
        while(temp < 0 or temp > 1):
            temp = float(input(f"Please enter a value between 0.0 and 1.0 for {skills[el]} : "))
        list.append(temp)
    
    index.update(id, list, namespace=namespace)
    return list