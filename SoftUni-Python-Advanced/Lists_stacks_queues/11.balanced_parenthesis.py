from collections import deque

given_parenthesis = deque(input())
# Check if parentheses are balanced
balanced_parenthesis = True
stack = deque()


matching_parentheses = {')': '(', '}': '{', ']': '['}

while given_parenthesis:
    char = given_parenthesis.popleft()
    if char in matching_parentheses.values():
        stack.append(char)
    elif char in matching_parentheses.keys():
        if stack and stack[-1] == matching_parentheses[char]:
            stack.pop()
        else:
            balanced_parenthesis = False
            break


if stack:
    balanced_parenthesis = False

if balanced_parenthesis:
    print("YES")
else:
    print("NO")





