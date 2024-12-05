string = input()

list_strings = string.split(", ")
# adding me in the list
list_strings.insert(len(list_strings),"me")
sheep_n = 0
for i in range(len(list_strings)-1, -1, -1):

    if list_strings[i] == "me" and list_strings[i - 1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if list_strings[i] == "sheep":
        sheep_n += 1
    elif list_strings[i] == "wolf":
        print(f'Oi! Sheep number {sheep_n}! You are about to be eaten by a wolf!')
        break


