# guests_info = {}
# command = input().split('-')
# unliked_meals = 0
# while command[0]!= "Stop":
#
#     if command[0] == "Like":
#         guest_name, meal_info = command[1], command[2]
#         if guest_name not in guests_info:
#             guests_info[guest_name] = {"liked_meals": []}
#             guests_info[guest_name]["liked_meals"].append(meal_info)
#         else:
#             guests_info[guest_name]["liked_meals"].append(meal_info)
#
#     elif command[0] == "Dislike":
#         guest_name, meal_info = command[1], command[2]
#         if guest_name not in guests_info:
#             print(f"{guest_name} is not at the party.")
#         else:
#             if meal_info not in guests_info[guest_name]["liked_meals"]:
#                 print(f"{guest_name} doesn't have the {meal_info} in his/her collection.")
#             else:
#                 guests_info[guest_name]["liked_meals"].remove(meal_info)
#                 unliked_meals += 1
#                 print(f"{guest_name} doesn't like the {meal_info}.")
#
#     command = input().split('-')
#
# for key, value in guests_info.items():
#     name = key
#     liked_meals = ", ".join(value["liked_meals"])
#     print(f"{name}: {liked_meals}")
# print(f"Unliked meals: {unliked_meals}")



guests_info = {}
unliked_meals = 0

while True:
    command = input().split('-')
    if command[0] == "Stop":
        break
    action, guest_name, meal_info = command[0], command[1], command[2]

    if action == "Like":
        if guest_name not in guests_info:
            guests_info[guest_name] = {"liked_meals": []}
        if meal_info not in guests_info[guest_name]["liked_meals"]:
            guests_info[guest_name]["liked_meals"].append(meal_info)

    elif action == "Dislike":
        if guest_name not in guests_info:
            print(f"{guest_name} is not at the party.")
        elif meal_info not in guests_info[guest_name]["liked_meals"]:
            print(f"{guest_name} doesn't have the {meal_info} in his/her collection.")
        else:
            guests_info[guest_name]["liked_meals"].remove(meal_info)
            unliked_meals += 1
            print(f"{guest_name} doesn't like the {meal_info}.")


for guest, info in guests_info.items():
    liked_meals = ", ".join(info["liked_meals"])
    print(f"{guest}: {liked_meals}")


print(f"Unliked meals: {unliked_meals}")

