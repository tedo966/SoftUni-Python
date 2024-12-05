my_string = input()
text = input()
while my_string in text:
    text = text.replace(my_string, "")
print(text)