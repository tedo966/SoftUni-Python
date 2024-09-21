number_of_ch = int(input())
result = 0
for index in range(number_of_ch):
    current_letter = input()
    result += ord(current_letter)
print(f'The sum equals: {result}')