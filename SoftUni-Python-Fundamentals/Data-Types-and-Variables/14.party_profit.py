from math import floor

group_size = int(input())
days = int(input())
coins = 0
spent_coins = 0
if group_size > 100 or days > 100:
    exit()
for current_day in range(1,days + 1):
    coins += 50
    if current_day % 15 == 0:
        group_size += 5
    if current_day % 10 == 0:
        group_size -= 2
    coins -= group_size * 2 # for food everyday
    if current_day % 3 == 0:
        spent_coins += group_size * 3
    if current_day % 5 == 0:
        coins += group_size * 20 # because you slay a boss
        if current_day % 3 == 0:
            spent_coins += group_size * 2  # because you have motivational party with comps

coins_per_comp = (coins - spent_coins) / group_size
print(f"{group_size} companions received {floor(coins_per_comp)} coins each.")

