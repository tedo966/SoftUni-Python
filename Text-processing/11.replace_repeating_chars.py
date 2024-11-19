my_chars = input()
result = ""
las_added_chr = ""
for char in my_chars:
    if char != las_added_chr:
        result += char
        las_added_chr = char
print(result)

