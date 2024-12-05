text = input()
text_result = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(text_result))