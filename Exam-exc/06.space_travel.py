travel_route = input().split("||")
amount_fuel = int(input())
amount_ammunition = int(input())
for element in travel_route:
    command = element.split()

    if command[0] == "Travel":
        distance = int(command[1])
        if distance <= amount_fuel:
            amount_fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            exit()

    elif command[0] == "Enemy":
        enemy_armor = int(command[1])
        if amount_ammunition >= enemy_armor:
            amount_ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            needed_fuel_to_escape = enemy_armor * 2
            if amount_fuel >= needed_fuel_to_escape:
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                exit()

    elif command[0] == "Repair":
        added_fuel = int(command[1])
        amount_fuel += added_fuel
        added_ammunition = added_fuel * 2
        amount_ammunition += added_ammunition
        print(f"Ammunitions added: {added_ammunition}.")
        print(f"Fuel added: {added_fuel}.")

    elif command[0] == "Titan":
        print("You have reached Titan, all passengers are safe." )
        exit()
