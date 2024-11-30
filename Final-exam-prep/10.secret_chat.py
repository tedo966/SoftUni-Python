concealed_message = input()
command = input().split(":|:")
while True:
    if command[0] == "Reveal":
        break
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action == "Reverse":
        current_string = command[1]
        if current_string in concealed_message:
            new_string = current_string[::-1]
            concealed_message = concealed_message.replace(current_string, new_string)
            print(concealed_message)
        else:
            print("error")

    elif action == "ChangeAll":
        old_letter = command[1]
        new_letter = command[2]
        concealed_message = concealed_message.replace(old_letter, new_letter)
        print(concealed_message)

    command = input().split(":|:")

print(f"You have a new text message: {concealed_message}")