numbers_as_string = input().split()
numbers_as_int = []
for num in numbers_as_string:
    numbers_as_int.append(int(num))

is_even = lambda x: x % 2 == 0 # check if numbers are even with lambda function
final_list = list(filter(is_even,numbers_as_int)) # convert to list and filter function lambda from numbers_as_int
print(final_list)

