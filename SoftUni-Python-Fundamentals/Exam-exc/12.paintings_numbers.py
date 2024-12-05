numbers_of_paintings = input().split()
while True:
    command = input()
    tokens = command.split()
    if command == "END":
        break
    if tokens[0] == "Change":
        number = tokens[1]
        new_number = tokens[2]
        if number in numbers_of_paintings:
            numbers_of_paintings[numbers_of_paintings.index(number)] = new_number
    elif tokens[0] == "Hide":
        number = tokens[1]
        if number in numbers_of_paintings:
            numbers_of_paintings.remove(number)
    elif tokens[0] == "Switch":
        number_1 = tokens[1]
        number_2 = tokens[2]
        if number_1 in numbers_of_paintings and number_2 in numbers_of_paintings:
            index_1 = numbers_of_paintings.index(number_1)
            index_2 = numbers_of_paintings.index(number_2)
            numbers_of_paintings[index_1], numbers_of_paintings[index_2] = numbers_of_paintings[index_2], numbers_of_paintings[index_1]
    elif tokens[0] == "Insert":
        if len(numbers_of_paintings) >= int(tokens[1]):
            number = tokens[2]
            index = int(tokens[1]) + 1
            numbers_of_paintings.insert(index, number)
    elif tokens[0] == "Reverse":
        numbers_of_paintings.reverse()
result_paintings = " ".join(numbers_of_paintings)
print(result_paintings)