beggars_income = input().split(", ")
count_beggars = int(input())
beggars_income_integer = []
for i in beggars_income: #convert to integer from string the beggars income
    beggars_income_integer.append(int(i))

list_of_beggars_income = []
start_index = 0
for current_beggar in range(count_beggars):
    current_beggar_sum = 0 #the sum of the income for the current beggar
    for current_index in range(start_index,len(beggars_income_integer), count_beggars):
        current_beggar_sum += beggars_income_integer[current_index] # we add income to the current beggar
    list_of_beggars_income.append(current_beggar_sum)
    start_index += 1 # we increase the start index (that's the next beggar)
print(list_of_beggars_income)


