students = {}

my_list = []
current_course = ""
command = input()
while True:
    my_list.append(command)
    command = input()
    if not ":" in command:
        current_course = command.strip().replace("_", " ")
        break
for current_student_course in my_list:
    if current_course in current_student_course:
        tokens = current_student_course.split(":")
        student_name = tokens[0]
        course_grade = int(tokens[1])
        students[student_name] = course_grade

for student, grade in students.items():
    print(f"{student} - {grade}")



