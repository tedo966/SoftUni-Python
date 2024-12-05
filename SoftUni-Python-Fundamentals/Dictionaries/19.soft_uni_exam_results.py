user_points_dictionary = {}
courses_dictionary = {}

while True:
    result = input().split("-")
    if len(result) == 1:
        break
    elif len(result) == 2:
        banned_name = result[0]
        del user_points_dictionary[banned_name]
    else:
        name, course, points = result[0], result[1], int(result[2])
        if name not in user_points_dictionary:
            user_points_dictionary[name] = 0
        if points > user_points_dictionary[name]:
            user_points_dictionary[name] = points
        if course not in courses_dictionary.keys():
            courses_dictionary[course] = 0
        courses_dictionary[course] += 1
print("Results:")
for name, points in user_points_dictionary.items():
    print(f"{name} | {points}")
print("Submissions:")
for course, submissions in courses_dictionary.items():
    print(f"{course} - {submissions}")
