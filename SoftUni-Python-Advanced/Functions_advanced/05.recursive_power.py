def recursive_power(number, pow):

    if pow == 0:
        return 1
    else:
        return number * recursive_power(number, pow- 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))