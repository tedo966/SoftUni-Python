import re
def add_my_plants():
    for count_plant in range(1, count_plants + 1):
        current_plant = input().split("<->")
        if current_plant[0] not in plants_info:
            plant, rarity = current_plant[0], int(current_plant[1])
            plants_info[plant] = {"rarity": rarity, "rating": 0, "count_rate": 0}
        else:
            plant, rarity = current_plant[0], int(current_plant[1])
            plants_info[plant]["rarity"] = rarity


def update_my_plants():
    while True:
        command = input()
        tokens = re.split(r"[-:\s+]+", command)

        if command == "Exhibition":
            break
        if tokens[1] not in plants_info:
            print("error")

        elif tokens[0] == "Rate":
            plant, add_rate = tokens[1], int(tokens[2])
            plants_info[plant]["rating"] += add_rate
            plants_info[plant]["count_rate"] += 1

        elif tokens[0] == "Update":
            plant, new_rarity = tokens[1], int(tokens[2])
            plants_info[plant]["rarity"] = new_rarity

        elif tokens[0] == "Reset":
            plant = tokens[1]
            plants_info[plant]["rating"] = 0
            plants_info[plant]["count_rate"] = 0


def check_my_list_plants():
    print("Plants for the exhibition:")
    for plant, rarity in plants_info.items():
        avg_rate = 0
        if plants_info[plant]['rating'] > 0:
            avg_rate = plants_info[plant]['rating'] / plants_info[plant]['count_rate']
        print(f"- {plant}; Rarity: {plants_info[plant]['rarity']}; Rating: {avg_rate:.2f}")


plants_info = {}
count_plants = int(input())
add_my_plants()
update_my_plants()
check_my_list_plants()


# n = int(input())
# plants = {}
#
# for _ in range(n):
#     name, rarity = input().split('<->')
#     rarity = int(rarity)
#     plants[name] = {"rarity": rarity, "ratings": []}
#
# while True:
#     line = input()
#     if line == 'Exhibition':
#         break
#     command = line.split(': ')
#     if command[0] == 'Rate':
#         try:
#             name, rating = command[1].split(' - ')
#             rating = float(rating)
#             if name in plants:
#                 plants[name]["ratings"].append(rating)
#             else:
#                 print("error")
#         except ValueError:
#             print("error")
#     elif command[0] == 'Update':
#         try:
#             name, new_rarity = command[1].split(' - ')
#             new_rarity = int(new_rarity)
#             if name in plants:
#                 plants[name]["rarity"] = new_rarity
#             else:
#                 print("error")
#         except ValueError:
#             print("error")
#     elif command[0] == 'Reset':
#         name = command[1]
#         if name in plants:
#             plants[name]["ratings"] = []
#         else:
#             print("error")
#     else:
#         print("error")
#
# print('Plants for the exhibition:')
# for name, details in plants.items():
#     average_rating = sum(details["ratings"]) / len(details["ratings"]) if details["ratings"] else 0
#     print(f'- {name}; Rarity: {details["rarity"]}; Rating: {average_rating:.2f}')