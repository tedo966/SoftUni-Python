from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
matches = 0
worms_size = len(worms)
while worms and holes:
    curr_worm = worms.pop()
    curr_hole = holes.popleft()

    if curr_worm > curr_hole or curr_hole > curr_worm:
        curr_worm -= 3
        if curr_worm > 0:
            worms.append(curr_worm)
            continue
    elif curr_worm == curr_hole:
        matches += 1

print(f"Matches: {matches}" if matches != 0 else "There are no matches.")


if matches != worms_size:
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
else:
    print("Every worm found a suitable hole!")

if not holes:
    print("Holes left: none")
elif holes:
    print(f"Holes left:", ', '.join(map(str,holes)))

# print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")
