expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        # we add to the stack the indexes of the ( matches
        stack.append(index)
    elif expression[index] == ")":
        # we extract from the stack list the  index of the first matched (
        start_index = stack.pop()
        # we find the end index when match the ) and we add 1 because its exclusive
        end_index = index + 1
        print(expression[start_index:end_index])