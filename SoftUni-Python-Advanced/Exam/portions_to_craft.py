from collections import deque

last_stored_substance = [int(x) for x in input().split(", ")]
crystals = deque(int(x) for x in input().split(", "))

potions = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}

crafted_potions = []

while last_stored_substance and crystals and len(crafted_potions) < len(potions):
    curr_substance = last_stored_substance.pop()
    curr_crystal = crystals.popleft()
    current_potion_energy = curr_substance + curr_crystal


    crafted = False
    for potion, energy in potions.items():
        if potion in crafted_potions:
            continue
        if current_potion_energy == energy:
            crafted_potions.append(potion)
            crafted = True
            break

    if not crafted:
        for potion, energy in sorted(potions.items(), key=lambda x: -x[1]):
            if potion in crafted_potions:
                continue
            if current_potion_energy > energy:
                crafted_potions.append(potion)
                curr_crystal -= 20
                if curr_crystal > 0:
                    crystals.append(curr_crystal)
                crafted = True
                break

    if not crafted:
        curr_crystal -= 5
        if curr_crystal > 0:
            crystals.append(curr_crystal)

all_potions_crafted = len(crafted_potions) == len(potions)


if all_potions_crafted:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print("Crafted potions: " + ", ".join(crafted_potions))

if last_stored_substance:
    print("Substances: " + ", ".join(map(str, reversed(last_stored_substance))))

if crystals:
    print("Crystals: " + ", ".join(map(str, crystals)))









