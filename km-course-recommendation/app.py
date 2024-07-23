import csv

# Step 1: Read the CSV files
def read_csv(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

workers = read_csv('workers.csv')
courses = read_csv('courses.csv')

# Step 2: Find the user based on the input names
def find_user(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    for person in workers:
        if person['name'].lower() == full_name.lower():
            return person
    return None

# Step 3: Recommend courses based on the user's level
def recommend_courses(level, main_language):
    recommendations = []
    for course in courses:
        if course['level'] == level:
            if main_language.lower() in course['category'].lower():
                recommendations.append(course)
    return recommendations

# Step 4: Main CLI logic
def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    
    user = find_user(first_name, last_name)
    
    if not user:
        print("User not found.")
        return
    
    level_map = {
        '0': 'Intern to Junior',
        '1': 'Junior to Mid',
        '2': 'Mid to Senior',
        '3': 'Mid/Senior to Senior'
    }
    
    level = level_map[user['level']]
    main_language = user['main_language']
    
    print(f"\nCourses recommended for {user['name']} ({user['position']} - {level}):\n")
    
    recommendations = recommend_courses(level, main_language)
    
    for course in recommendations:
        print(f"Course Name: {course['course_name']}")
        print(f"Description: {course['description']}")
        print(f"URL: {course['url']}\n")

if __name__ == "__main__":
    main()
