words = ['luxuriant', 'silly', 'dizzy', 'frightening', 'blink', 'silly', 'enjoy',
               'suspend', 'blink', 'reward', 'blink', 'fact',
               'debt', 'marble', 'blink', 'yak', 'frightening', 'suspend', 'debt']

my_dict = {}

for index in range(len(words)):
    my_dict[words[index]] = 0
    for word in words:
        current_word = words[index]
        if current_word == word:
            my_dict[current_word] += 1

for word, count in my_dict.items():
    print(f"{word}: |{'*' * count}")
