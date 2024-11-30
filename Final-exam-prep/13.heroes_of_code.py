number_of_heroes_chose = int(input())
my_heroes = {}
for _ in range(number_of_heroes_chose):
    hero_info = input().split()
    hero_name = hero_info[0]
    hero_hp = int(hero_info[1])
    hero_mana = int(hero_info[2])
    my_heroes[hero_name] = {"hp": int(hero_hp), "mana": int(hero_mana)}
command = input().split(" - ")
while command[0]!= "End":
    if command[0] == "CastSpell":
        hero = command[1]
        mana_needed = int(command[2])
        spell_name = command[3]
        if my_heroes[hero]["mana"] >= mana_needed:
            my_heroes[hero]["mana"] -= mana_needed
            print(f"{hero} has successfully cast {spell_name} and now has {my_heroes[hero]['mana']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        my_heroes[hero]["hp"] -= damage
        if not my_heroes[hero]["hp"] <= 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {my_heroes[hero]['hp']} HP left!")
        else:
            del my_heroes[hero]
            print(f'{hero} has been killed by {attacker}!')

    elif command[0] == "Recharge":
        hero = command[1]
        mana_recharge = int(command[2])
        if my_heroes[hero]['mana'] + mana_recharge >= 200:
            mana_recharge_for = 200 - my_heroes[hero]['mana']
            my_heroes[hero]['mana'] = 200
            print(f"{hero} recharged for {mana_recharge_for} MP!")
        else:
            my_heroes[hero]['mana'] += mana_recharge
            print(f"{hero} recharged for {mana_recharge} MP!")

    elif command[0] == "Heal":
        hero = command[1]
        heal_amount = int(command[2])
        if my_heroes[hero]['hp'] + heal_amount >= 100:
            healed_for = 100 - my_heroes[hero]['hp']
            my_heroes[hero]["hp"] = 100
            print(f"{hero} healed for {healed_for} HP!")

        else:
            my_heroes[hero]['hp'] += heal_amount
            print(f"{hero} healed for {heal_amount} HP!")

    command = input().split(" - ")

for hero in my_heroes.keys():
    print(f"{hero}")
    print(f"HP: {my_heroes[hero]['hp']}")
    print(f"MP: {my_heroes[hero]['mana']}")