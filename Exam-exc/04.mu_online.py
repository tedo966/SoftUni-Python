# rooms = input().split("|")
# health = 100
# room = 1
# bitcoins = 0
# for tokens in rooms:
#     tokens = tokens.split()
#     if tokens[0] == "potion":
#         if health < 100:
#             health += int(tokens[1])
#             if health >= 100:
#                 print(f"You healed for {int(tokens[1]) - (health % 100)} hp.")
#                 health = 100
#                 print(f"Current health: {health} hp.")
#             else:
#                 print(f"You healed for {tokens[1]} hp.\nCurrent health: {health} hp.")
#
#     elif tokens[0] == "chest":
#         bitcoins += int(tokens[1])
#         print(f"You found {tokens[1]} bitcoins.")
#     else:
#         health -= int(tokens[1])
#         monster = tokens[0]
#         if health <= 0:
#             print(f"You died! Killed by {monster}.\nBest room: {room}" )
#             exit()
#         else:
#             print(f"You slayed {monster}.")
#     room += 1
#
# print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")

rooms = input().split("|")
health = 100
room = 1
bitcoins = 0

for tokens in rooms:
    tokens = tokens.split()
    command = tokens[0]
    value = int(tokens[1])

    if command == "potion":
        healed_amount = min(100 - health, value)
        health += healed_amount
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        monster = command
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room}")
            exit()
    room += 1

print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")




