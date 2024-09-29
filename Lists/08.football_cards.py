cards = input().split()
a_team_loses = []
b_team_loses = []
for current_card in cards:
    if len(a_team_loses) > 4 or len(b_team_loses) > 4:
        break
    if current_card in a_team_loses:
        continue
    elif current_card in b_team_loses:
        continue
    if "A" in current_card:
        a_team_loses.append(current_card)
    elif "B" in current_card:
        b_team_loses.append(current_card)
a_players = 11 - len(a_team_loses)
b_players = 11 - len(b_team_loses)
print(f'Team A - {a_players}; Team B - {b_players}')
if a_players < 7 or b_players < 7:
    print("Game was terminated")




