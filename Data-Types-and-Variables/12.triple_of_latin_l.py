number_of_symbols = int(input())
for first_n in range(97,97 + number_of_symbols):
    for second_n in range(97,97 + number_of_symbols):
        for third_n in range(97,97 + number_of_symbols):
            print(f'{chr(first_n)}{chr(second_n)}{chr(third_n)}')