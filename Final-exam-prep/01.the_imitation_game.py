def crack_enigma_code():
    encrypted_message = input()
    command = input()
    while True:
        if command == "Decode":
            break

        command_parts = command.split('|')
        action = command_parts[0]

        if action == "Move":
            count_letters = int(command_parts[1])
            encrypted_message = encrypted_message[count_letters:] + encrypted_message[:count_letters]

        elif action == "Insert":
            index = int(command_parts[1])
            insert_letter = command_parts[2]
            encrypted_message = encrypted_message[:index] + insert_letter + encrypted_message[index:]
        elif action == "ChangeAll":
            check_letter = command_parts[1]
            new_letter = command_parts[2]
            encrypted_message = encrypted_message.replace(check_letter, new_letter)

        command = input()

    print(f'The decrypted message is: {encrypted_message}')


crack_enigma_code()

