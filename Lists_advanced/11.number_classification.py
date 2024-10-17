
def positive_nums(nums):
    return ", ".join([num for num in nums if int(num) >= 0])

def negative_nums(nums):
    return ", ".join([num for num in nums if int(num) < 0])

def even_nums(nums):
    return ", ".join([num for num in nums if int(num) % 2 == 0])

def odd_nums(nums):
    return ", ".join([num for num in nums if int(num) % 2!= 0])


list_of_numbers = input().split(', ')
print(f'Positive: {positive_nums((list_of_numbers))}')
print(f'Negative: {negative_nums((list_of_numbers))}')
print(f'Even: {even_nums((list_of_numbers))}')
print(f'Odd: {odd_nums(list_of_numbers)}')

