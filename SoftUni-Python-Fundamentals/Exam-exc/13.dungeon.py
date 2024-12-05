needed_exp = int(input())
count_of_battles = int(input())
my_exp = 0
battles = 0
the_exp_is_enough = False
for current_battle in range(1, count_of_battles + 1):
    exp_for_current_battle = int(input())
    battles += 1

    if current_battle % 15 == 0:
        my_exp += exp_for_current_battle + (exp_for_current_battle * 0.05)
    elif current_battle % 5 == 0:
        my_exp += exp_for_current_battle - (exp_for_current_battle * 0.10)
    elif current_battle % 3 == 0:
        my_exp += exp_for_current_battle + (exp_for_current_battle * 0.15)
    else:
        my_exp += exp_for_current_battle

    if my_exp >= needed_exp:
        the_exp_is_enough = True
        break

if the_exp_is_enough:
    print(f"Player successfully collected his needed experience for {battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_exp - my_exp:.2f} more needed.")