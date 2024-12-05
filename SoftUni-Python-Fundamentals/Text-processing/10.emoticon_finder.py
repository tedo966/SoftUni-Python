my_text = input()
for index in range(0, len(my_text)):
    if my_text[index] == ":":
        print(f":{my_text[index + 1]}")
