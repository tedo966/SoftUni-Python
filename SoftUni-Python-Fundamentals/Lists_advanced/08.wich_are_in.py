# 1
# def find_substrings(first_list, second_list):
#     result = []
#     for substring in first_list:
#         if any(substring in string for string in second_list):
#             result.append(substring)
#     return result
#
# first_input = input().split(', ')
# second_input = input().split(', ')
#
# result = find_substrings(first_input, second_input)
# print(result)

# 1.1
first_sequence = input().split()
second_sequence = input().split()
result = []

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            result.append(first_string)
            break
print(result)

# 1.2

# 1.3
# first_sequence = input().split(', ')
# second_sequence = input().split(', ')
# result = [first_string for first_string in first_sequence if any(first_string in second_string for second_string in second_sequence)]
# print(result)