import re
text_string = input()
pattern = r'([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
matches = re.findall(pattern, text_string)
list_pairs = []
for index in range(0, len(matches)):
    first_word = matches[index][1]
    second_word = matches[index][2][::-1]
    if first_word == second_word:
        list_pairs.append(f'{first_word} <=> {second_word[::-1]}')
list_pairs = ', '.join(list_pairs)
if len(matches) <= 0:
    print('No word pairs found!')
else:
    print(f'{len(matches)} word pairs found!')
if list_pairs:
    print(f'The mirror words are:\n{list_pairs}')
else:
    print('No mirror words!')





