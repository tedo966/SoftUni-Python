divisor = int(input())
bound = int(input())
while bound != 0:
    largest_n = bound % divisor
    if largest_n == 0:
        print(bound)
        break
    bound -= 1




