def characters_between_with_space(first_char: str, second_char: str) -> str:
    # Generate the characters between first_char and second_char
    characters = [chr(i) for i in range(ord(first_char) + 1, ord(second_char))]

    # Join the characters with a space
    return ' '.join(characters)


# Get input from the user
first_char = input()
second_char = input()

# Print the result
print(characters_between_with_space(first_char, second_char))



