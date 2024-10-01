my_gifts = input().split()
my_list = []
command = input()
while command != "No Money":
    command_parts = command.split()
    if "OutOfStock" in command_parts and command_parts[1] in my_gifts:
        for i in range(len(my_gifts)):
            if my_gifts[i] == command_parts[1]:
                my_gifts[i] = "None"
    elif "Required" in command_parts:
        index_check = int(command_parts[2])
        if 0 <= index_check < len(my_gifts):
            my_gifts[index_check] = command_parts[1]
    elif "JustInCase" in command_parts:
        my_gifts[-1] = command_parts[1]

    command = input()
for element in my_gifts:
    if element != "None":
        my_list.append(element)
print(" ".join(my_list))



