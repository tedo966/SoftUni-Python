# from collections import deque
# quantity_of_water = int(input())
# people = deque()
# command = input()
# while command != "Start":
#     people.append(command)
#     command = input()
#
# command = input()
# while command != "End":
#     if command.isdigit():
#         liters = int(command)
#         if quantity_of_water - liters >= 0:
#             quantity_of_water -= liters
#             person = people.popleft()
#             print(f"{person} got water")
#         else:
#             person = people.popleft()
#             print(f"{person} must wait")
#     else:
#         command = command.split()
#         token = command[0]
#         if token == "refill":
#             quantity_of_water += int(command[1])
#
#     command = input()
#
# print(f"{quantity_of_water} liters left")

from collections import deque

liters = int(input())

people = deque()

name = input()

while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    if command.startswith("refill"):
        _, liters_to_refill = command.split()
        liters_to_refill = int(liters_to_refill)
        liters += liters_to_refill
    else:
        liters_requested = int(command)
        name = people.popleft()
        if liters_requested <= liters:
            liters -= liters_requested
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

    command = input()


print(f"{liters} liters left")