list_of_numbers = input().split()
to_remove = int(input())
integer_list = []
for number in list_of_numbers:
    integer_list.append(int(number))
# Remove the smallest numbers
for _ in range(to_remove):
    integer_list.remove(min(integer_list))

# Print the remaining numbers separated by ", "
print(", ".join(map(str, integer_list)))