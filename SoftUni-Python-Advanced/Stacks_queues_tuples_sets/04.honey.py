from collections import deque

bees_count = deque(map(int, input().split()))
nectar_values = list(map(int, input().split()))
symbols = deque(input().split())

honey_made = 0

while bees_count and nectar_values:
    current_bee = bees_count[0]
    last_nectar = nectar_values[-1]

    if last_nectar >= current_bee:
        bees_count.popleft()
        nectar = nectar_values.pop()
        symbol = symbols.popleft()

        if symbol == "+":
            honey_made += current_bee + nectar
        elif symbol == "-":
            honey_made += abs(current_bee - nectar)
        elif symbol == "*":
            honey_made += current_bee * nectar
        elif symbol == "/" and nectar != 0:
            honey_made += current_bee / nectar

    else:
        nectar_values.pop()

print(f"Total honey made: {honey_made}")
if bees_count:
    print(f"Bees left: {', '.join(map(str, bees_count))}")
if nectar_values:
    print(f"Nectar left: {', '.join(map(str, nectar_values))}")









