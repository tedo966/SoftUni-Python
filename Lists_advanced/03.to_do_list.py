notes = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0]) - 1 # -1 because notes length is 10 but 9 indexes
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)
result = [element for element in notes if element != 0] # clear notes form 0's
print(result)