lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet = 0
sword = 0
shield = 0
armor = 0
shield_breaks = 0  # Keep track of how many times the shield has broken

for index_lost_fights in range(1, lost_fights + 1):

    if index_lost_fights % 2 == 0:
        helmet += helmet_price
    if index_lost_fights % 3 == 0:
        sword += sword_price
    if index_lost_fights % 2 == 0 and index_lost_fights % 3 == 0:
        shield += shield_price
        shield_breaks += 1  # Count how many times the shield has broken

    if shield_breaks > 0 and shield_breaks % 2 == 0:# Every second shield break
        shield_breaks = 0
        armor += armor_price

expenses_for_year = helmet + sword + shield + armor
print(f"Gladiator expenses: {expenses_for_year:.2f} aureus")


# lost_fight_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# broken_helmet = lost_fight_count // 2
# broken_sword = lost_fight_count // 3
# broken_shield = lost_fight_count // (2 * 3)
# broken_armor = broken_shield // 2
# expenses = broken_helmet * helmet_price \
#     + broken_sword * sword_price \
#     + broken_shield * shield_price \
#     + broken_armor * armor_price
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")