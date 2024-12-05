my_text = input()
encrypt_text = ""
for character in my_text:
    encrypt_text += chr((ord(character) + 3))
print(encrypt_text)

