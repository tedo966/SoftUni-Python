number = int(input())
number_to_str = str(number)

result = ""

while number_to_str:
    # find max num
    current_max = max(number_to_str)
    result += current_max
    # remove the maximum digit from the number string
    number_to_str = number_to_str.replace(current_max, '', 1)
result = int(result)
print(result)