working_days_events = input().split("|")
energy = 100
earned_coins = 100
for event in range(len(working_days_events)):
    day_event = working_days_events[event].split("-")
    command = day_event[0]
    num_in_day_event = int(day_event[1])

    if command == "rest":
        #ensures that the energy gained does not exceed 100, and only the necessary amount of energy is added.
        gained_energy = min(100 - energy, num_in_day_event)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif command == "order":
        if energy >= 30:
            energy -= 30
            earned_coins += num_in_day_event
            print(f"You earned {num_in_day_event} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if earned_coins >= num_in_day_event:
            earned_coins -= num_in_day_event
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            exit()
print(f"Day completed!\nCoins: {earned_coins}\nEnergy: {energy}")




