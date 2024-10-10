def factorial_of_number(num1: int, num2: int) -> float:
    factorial_num1 = 1
    factorial_num2 = 1

    for multiplier in range(num1, 1, -1):
        factorial_num1 *= multiplier

    for multiplier in range(num2, 1, -1):
        factorial_num2 *= multiplier

    return factorial_num1 / factorial_num2

first_num = int(input())
second_num = int(input())
result = factorial_of_number(first_num, second_num)
print(f"{result:.2f}")

# import math
# 
# def factorial_of_number(num1: int, num2: int) -> float:
#     factorial_num1 = math.factorial(num1)
#     factorial_num2 = math.factorial(num2)
#     return factorial_num1 / factorial_num2
#
# first_num = int(input())
# second_num = int(input())
# result = factorial_of_number(first_num, second_num)
# print(f"{result:.2f}")

