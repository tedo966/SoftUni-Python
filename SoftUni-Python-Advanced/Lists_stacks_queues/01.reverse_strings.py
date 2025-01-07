my_string = list(input())
while my_string:
    #pops and prints the popped char from the string in the same line using end
    print(my_string.pop(), end="")



# another way to solve the problem using appennd and pop
# text = list(input())
# stack = []
# for i in range(len(text)):
#     stack.append(text.pop())
# print("".join(stack))