lines = int(input())
stack = []

for _ in range(lines):
    current_line = input().split()
    command = int(current_line[0])

    if command == 1:
        stack.append(int(current_line[1]))
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

# Print the stack from top to bottom in the specified format
print(", ".join(map(str, reversed(stack))))