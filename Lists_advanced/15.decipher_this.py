def decipher_message(message):
    words = message.split()
    deciphered_words = []

    for word in words:
        # Extract the initial number and the rest of the characters
        number = ""
        chars = ""
        for char in word:
            if char.isdigit():
                number += char
            else:
                chars += char

        # Convert the initial number to a character
        first_char = chr(int(number))

        # Swap the second and last characters
        if len(chars) > 1:
            chars = chars[-1] + chars[1:-1] + chars[0]

        # Form the deciphered word
        deciphered_word = first_char + chars
        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)

message = input()
deciphered = decipher_message(message)
print(deciphered)

