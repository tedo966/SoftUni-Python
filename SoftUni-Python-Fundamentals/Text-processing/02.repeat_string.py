my_string = input().split(" ")
result = ""
for word in my_string:
    result += len(word) * word
print(result)