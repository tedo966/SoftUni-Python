number_of_students = int(input())
count_lectures = int(input())
additional_bonus =  int(input())
student_attendance = 0
max_bonus = 0
for students in range(number_of_students):
    current_student = int(input())
    student_bonus = current_student / count_lectures * (5 + additional_bonus)
    if student_bonus > max_bonus:
        student_attendance = current_student
        max_bonus = student_bonus
print(f"Max Bonus: {max_bonus.__ceil__()}.")
print(f"The student has attended {student_attendance} lectures.")



