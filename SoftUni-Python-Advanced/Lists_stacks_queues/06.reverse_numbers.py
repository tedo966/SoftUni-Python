my_nums = input().split()
my_stack = []
while my_nums:
    my_stack.append(my_nums.pop())
print(" ".join(my_stack))