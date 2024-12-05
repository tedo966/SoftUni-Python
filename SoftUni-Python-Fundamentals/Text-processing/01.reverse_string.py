my_string = input()
while not my_string == "end":
    reversed_string = my_string[::-1]
    print(f"{my_string} = {reversed_string}")
    my_string = input()