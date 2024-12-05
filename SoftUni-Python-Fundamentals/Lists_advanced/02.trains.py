wagons = int(input()) * [0]
commands = input().split()
while commands [0] != "End":
    current_command = commands[0]
    if current_command == "add":
        wagons[-1] += int(commands[1])
    elif current_command == "insert":
        i = int(commands[1])
        current_persons = int(commands[2])
        wagons[i] += current_persons
    elif current_command == "leave":
        i = int(commands[1])
        removed_persons = int(commands[2])
        wagons[i] -= removed_persons
    commands = input().split()
print(wagons)