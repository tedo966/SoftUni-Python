while True:
    command = input()
    if command == "SoftUni":
        continue
    elif command == "End":
        exit()
    else:
        for i in command:
            print(i * 2, end="")
        print()





