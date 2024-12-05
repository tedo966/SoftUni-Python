current_line = input()
courses_dict = {}
while current_line != "end":
    tokens = current_line.split(" : ")
    course_name = tokens[0]
    student = tokens[1]
    if course_name not in courses_dict:
        courses_dict[course_name] = []
    courses_dict[course_name].append(student)
    current_line = input()


for course_name, students in courses_dict.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")

