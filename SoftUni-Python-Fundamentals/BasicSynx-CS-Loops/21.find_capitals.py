from curses.ascii import isupper
word = input()
result = []
for i in range(len(word)):
    if isupper(word[i]):
        result.insert(len(word),i)
    else:
        continue
print(result)