list_elements = input().split()
combinations = input()
turns = 0

while True:
    if not list_elements:
        print(f"You have won in {turns} turns!")
        break

    if combinations == "end":
        print(f"Sorry you lose :(\n{' '.join(list_elements)}")
        break
    turns += 1
    tokens = combinations.split()
    first_element = int(tokens[0])
    second_element = int(tokens[1])

    if (first_element == second_element or
        first_element >= len(list_elements) or
        second_element >= len(list_elements) or
        first_element < 0 or
        second_element < 0):
        print("Invalid input! Adding additional elements to the board")
        middle_index = len(list_elements) // 2
        extra_element = f"-{turns}a"
        list_elements.insert(middle_index, extra_element)
        list_elements.insert(middle_index + 1, extra_element)

    elif list_elements[first_element] == list_elements[second_element]:
        print(f"Congrats! You have found matching elements - {list_elements[first_element]}!")
        list_elements.pop(first_element)
        if first_element < second_element:
            second_element -= 1
        list_elements.pop(second_element)
    else:
        print("Try again!")

    combinations = input()


