import matplotlib.pyplot as plt
from CRUD.read import query_vector_id
from recommender import recommender


def employee_skills_plot(employee_id, target_position_id):
    employee = query_vector_id(employee_id, 'employees')[0]
    current_hard_skills, current_soft_skills = (i*100 for i in employee.get('values'))

    target_pos = query_vector_id(target_position_id, 'positions')[0]
    target_hard_skills, target_soft_skills = (i*100 for i in target_pos.get('values'))

    courses_category = []
    courses_skills = []

    output = recommender(target_position_id)
    courses_list = output.split('\n')[4:]

    for course in courses_list:
        vec = (query_vector_id(course, 'courses')[0]).get("values")
        vec = [i*100 for i in vec]
        vec_metadata = (query_vector_id(course, 'courses')[0]).get("metadata").get("Category")
        courses_skills.append(vec)
        courses_category.append(vec_metadata)


    time_points = [0]
    hard_skills = [current_hard_skills]
    soft_skills = [current_soft_skills]
    courses_taken = ["Start"]

    if current_hard_skills < target_hard_skills:
        category_to_recommend = 'Hard'
    else:
        category_to_recommend = 'Soft'


    current_values = [current_hard_skills, current_soft_skills]
    for i, add_value in enumerate(courses_skills):
        current_course_category = courses_category[i]

        if category_to_recommend != current_course_category:
            continue

        if category_to_recommend == "Hard":
            current_values[0] += add_value[0]
            current_values[1] -= add_value[0]
        else:
            current_values[0] -= add_value[1]
            current_values[1] += add_value[1]

        time_points.append(i + 1)
        hard_skills.append(current_values[0])
        soft_skills.append(current_values[1])
        courses_taken.append(courses_list[i])

        if current_values[0] >= target_hard_skills and category_to_recommend=="Hard":
            break
        elif current_values[1] >= target_soft_skills and category_to_recommend=="Soft":
            break

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(time_points, hard_skills, marker='o', label='Hard Skills')

    ax.plot(time_points, soft_skills, marker='o', label='Soft Skills')

    if category_to_recommend == "Hard":

        for i, txt in enumerate(courses_taken):
            ax.annotate(txt, (time_points[i], hard_skills[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    else:

        for i, txt in enumerate(courses_taken):
            ax.annotate(txt, (time_points[i], soft_skills[i]), textcoords="offset points", xytext=(0, -10), ha='center')

    employee_name = employee_id[:-9].replace("_", " ")

    ax.set_title(f"{employee_name}'s Skill Progress Over Time")

    ax.set_xlabel("Time(months)")
    ax.set_ylabel("Skill Percentage")
    ax.set_ylim(0, 100)
    ax.grid(True)
    ax.legend()

    return fig
