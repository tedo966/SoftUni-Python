import re

names = input()

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
valid_names = re.finditer(pattern, names)

for name in valid_names:
    print(name.group(), end=" ")