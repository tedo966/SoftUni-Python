pairs = int(input())
info_students = {}

for index in range(1, pairs +1):
    name = input()
    grade = float(input())
    if name not in info_students:
        info_students[name] = []
    info_students[name].append(grade)

for student, grade in info_students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")





