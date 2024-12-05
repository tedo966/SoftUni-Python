find_pass_text = input()
command = input()
while True:
    if command == "Done":
        password = find_pass_text
        print(f"Your password is: {password}")
        break
    if command == "TakeOdd":
        find_pass_text = find_pass_text[1::2]
        print(find_pass_text)
        command = input()
    else:
        command = command.split()

        if command[0] == "Cut":
            start_cut = int(command[1])
            stop_cut = int(command[2]) + start_cut
            find_pass_text = find_pass_text[:start_cut] + find_pass_text[stop_cut:]
            print(find_pass_text)
        elif command[0] == "Substitute":
            substring = command[1]
            substitute_text = command[2]
            if not substring in find_pass_text:
                print("Nothing to replace!")
            else:
                find_pass_text = find_pass_text.replace(substring, substitute_text)
                print(find_pass_text)

        command = input()







