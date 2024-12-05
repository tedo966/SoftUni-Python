numbers_as_string = input().split()
numbers_as_int = []

for num in numbers_as_string:
    numbers_as_int.append(int(num))
result_sorted = sorted(numbers_as_int)

print(result_sorted)