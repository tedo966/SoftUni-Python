from collections import deque

bees_group = deque([int(x) for x in input().split()])
bee_eaters_group = [int(x) for x in input().split()]

while bees_group and bee_eaters_group:
    current_bees_group = bees_group.popleft()
    current_bee_eater_group = bee_eaters_group.pop()

    if 7 * current_bee_eater_group > current_bees_group:
        current_bee_eater_group -= current_bees_group // 7
        bee_eaters_group.append(current_bee_eater_group)

    elif 7 * current_bee_eater_group < current_bees_group:
        current_bees_group -= current_bee_eater_group * 7
        bees_group.append(current_bees_group)
    else:
        continue

print("The final battle is over!")

if not bees_group and not bee_eaters_group:
    print("But no one made it out alive!")
elif bees_group:
    print(f"Bee groups left: {', '.join(map(str, bees_group))}")
elif bee_eaters_group:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_group))}")