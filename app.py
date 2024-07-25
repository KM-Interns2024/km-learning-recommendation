import csv
from CRUD.select_vector import query_id, query_course_rec
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
index = pc.Index("kbc")

def compare_values():
    pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
    index = pc.Index("kbc")

    skills = ["Python", "Java", "C++", "C", "C#", "JavaScript", "Ruby", "PHP", "Swift", "Objective-C", "R", "Perl", "Scala", "Go", "HTML", "CSS"]

    position_vec = query_id(namespace='positions')
    worker_vec = query_id(namespace='employees')

    for i in range(len(skills)):
        if(position_vec[i] > worker_vec[i]):
            print(query_course_rec(position_vec[i], skills[i]))

compare_values()
