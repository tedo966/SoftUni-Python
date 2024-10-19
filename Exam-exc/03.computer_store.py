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

memory_game_list = input().split()
moves = 1

# while True:
#     user_command = input().split()
#     if str(user_command[0]) == 'end':
#         break
#
#     first_number, second_number = int(user_command[0]), int(user_command[1])
#
#     if first_number == second_number or first_number < 0 or second_number < 0 or \
#             first_number > len(memory_game_list) - 1 or second_number > len(memory_game_list) - 1:
#         print("Invalid input! Adding additional elements to the board")
#         middle_of_list = len(memory_game_list) // 2
#         memory_game_list.insert(middle_of_list, f"{moves * -1}a")
#         memory_game_list.insert(middle_of_list, f"{moves * -1}a")
#     elif memory_game_list[first_number] == memory_game_list[second_number]:
#         matching_element = memory_game_list.pop(first_number)
#         memory_game_list.remove(matching_element)
#         print(f"Congrats! You have found matching elements - {matching_element}!")
#     else:
#         print("Try again!")
#
#     if not memory_game_list:
#         print(f"You have won in {moves} turns!")
#         break
#
#     moves += 1
#
# if memory_game_list:
#     print('Sorry you lose :(')
#     print(*memory_game_list)


