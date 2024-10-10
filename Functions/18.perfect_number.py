def perfect_num(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
        if sum_divisors == num:
            return "We have a perfect number!"
    return "It's not so perfect."

given_num = int(input())
print(perfect_num(given_num))