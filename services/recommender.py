from misc.api_key import api_key
from pinecone import Pinecone
from CRUD.operations import query_id


pc = Pinecone(api_key=api_key)



def compare_values():
    index = pc.Index("kbc")

    skills = ["Python", "Java", "C++", "C", "C#", "JavaScript", "Ruby", "PHP", "Swift", "Objective-C", "R", "Perl", "Scala", "Go", "HTML", "CSS"]

    position_vec = query_id()
    worker_vec = query_id()
    counter = 0

    for i in range(len(position_vec)):
        if(position_vec[i] > worker_vec[i]):
            course_rec(position_vec, i)