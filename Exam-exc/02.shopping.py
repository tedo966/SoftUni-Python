my_list = input().split("!")
command = input()
while command != "Go Shopping!":
    tokens = command.split()
    if tokens[0] == "Urgent":
        if tokens[1] not in my_list:
            my_list.insert(0, tokens[1])
    elif tokens[0] == "Unnecessary":
        if tokens[1] in my_list:
            my_list.remove(tokens[1])
    elif tokens[0] == "Correct":
        if tokens[1] in my_list:
            index = my_list.index(tokens[1])
            my_list[index] = tokens[2]
    elif tokens[0] == "Rearrange":
        if tokens[1] in my_list:
            my_list.remove(tokens[1])
            my_list.append(tokens[1])
    command = input()
result = ", ".join(my_list)
print(result)
