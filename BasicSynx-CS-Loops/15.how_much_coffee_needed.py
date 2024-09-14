command = input()
coffee_needed = 0
while command != "END":
    if (command == "coding" or command == "CODING"
            or command == "dog"
            or command == "DOG")\
            or command == "cat"\
            or command == "CAT"\
            or command == "movie"\
            or command == "MOVIE":
        if command.isupper() == True:
            coffee_needed += 2
        else:
            coffee_needed += 1
        command = input()
    else:
        command = input()
        continue
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)


