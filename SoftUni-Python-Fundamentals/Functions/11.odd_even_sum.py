def result_odd_even(nums_string):
    odd = 0
    even = 0
    for num in nums_string:
        num = int(num)
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return f'Odd sum = {odd}, Even sum = {even}'

string_nums = input()
print(result_odd_even(string_nums))