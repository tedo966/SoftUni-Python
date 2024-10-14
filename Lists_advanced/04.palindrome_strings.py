strings = input().split()
searched_palindrome = input()
palindromes = []
for string in strings:
    if string == string[::-1]: # we compare if reversed string is equal to normal string
        palindromes.append(string)
print(f'{palindromes}')
#we search how many times the searched palindrome is in palindromes list and print
print(f'Found palindrome {palindromes.count(searched_palindrome)} times')
