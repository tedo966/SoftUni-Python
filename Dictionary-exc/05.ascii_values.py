letters = input().split(", ")
values = []
for letter in letters:
    if letter.isalpha():
        values.append(ord(letter))
my_dictionary = {letter:value for (letter,value) in zip(letters,values)}
print(my_dictionary)