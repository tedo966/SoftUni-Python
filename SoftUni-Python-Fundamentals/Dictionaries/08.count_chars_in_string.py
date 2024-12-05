my_string = input().replace(" ", "")
chars_dictionary = {}
for char in my_string:
    if char not in chars_dictionary:
        chars_dictionary[char] = 1
    else:
        chars_dictionary[char] += 1
for char in chars_dictionary:
    print(f"{char} -> {chars_dictionary[char]}")



