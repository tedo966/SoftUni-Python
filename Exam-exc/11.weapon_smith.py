parts_weapon = input().split("|")
while True:
    command = input()
    if command == "Done":
        break
    tokens = command.split()

    if tokens[0] == "Add":
        index = int(tokens[2])
        if len(parts_weapon) -1 >= index and index >= 0:
            parts_weapon.insert(index, tokens[1])
    elif tokens[0] == "Remove":
        index = int(tokens[1])
        if len(parts_weapon) -1 >= index and index >= 0:
            parts_weapon.pop(index)
    elif tokens[1] == "Even":
        even_indexes = ""
        for index in range(len(parts_weapon)):
            if index % 2 == 0:
                even_indexes += parts_weapon[index] + " "
        print(even_indexes)
    elif tokens[1] == "Odd":
        odd_indexes = ""
        for index in range(len(parts_weapon)):
            if index % 2 == 1:
                odd_indexes += parts_weapon[index] + " "
        print(odd_indexes)
result = "".join(parts_weapon)
print(f"You crafted {result}!")



